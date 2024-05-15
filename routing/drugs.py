from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugOrm
from schemas import StoredDrug, UsedDrug, Drug

router = APIRouter(prefix="/drugs")


@router.get("/")
async def get_drugs(session: AsyncSession = Depends(get_session)) -> list[Drug]:
    query = select(DrugOrm)
    result = await session.execute(query)
    return [Drug.model_validate(i) for i in result.scalars().all()]


@router.get("/popular")
async def get_popular_drugs(limit: int = 10, drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)) -> list[UsedDrug]:
    tmp = "" if drug_type_id is None else f"where type_id = {drug_type_id}"

    query_string = f"""
        with
            used_in_cooking_drugs as (
                select
                    component_id as drug_id,
                    sum(component_amount) as drug_amount
                from production
                    join technology_components on production.technology_id = technology_components.technology_id
                    join drugs on technology_components.component_id = drugs.id
                where start is not null
                group by component_id
            ),
    
            sold_drugs as (
                select
                    drug_id,
                    sum(amount) as drug_amount
                from orders
                    join prescriptions_content using (prescription_id)
                where obtaining_datetime is not null
                group by drug_id
            ),
    
            used_drugs as (
                select
                    drug_id,
                    drugs.name,
                    sum(drug_amount) as drug_amount
                from (
                    select *
                    from used_in_cooking_drugs
                    union all
                    select *
                    from sold_drugs
                    ) as _
                    join drugs on drug_id = drugs.id
                {tmp}
                group by drug_id)
                
        select drug_id, drug_amount
        from used_drugs
        order by drug_amount desc
        limit {limit}
    """

    result = await session.execute(text(query_string))

    popular_drugs: list[UsedDrug] = []

    for i in result:
        d = await session.get(DrugOrm, ident=i[0])

        popular_drugs.append(UsedDrug(
            drug=Drug.model_validate(d),
            uses_number=i[1]
        ))

    return popular_drugs


@router.get("/critical-amount")
async def get_critical_amount_drugs(session: AsyncSession = Depends(get_session)) -> list[Drug]:
    query = text(
        """
        with
            critical_amount_drugs as (
                select
                    drugs.id as drug_id,
                    drugs.name as drug_name,
                    coalesce(sum(available_amount), 0) as drug_amount,
                    critical_amount
                from drugs
                    left join storage_items on drugs.id = storage_items.drug_id
                group by
                    drugs.id,
                    critical_amount
                having
                    drug_amount <= critical_amount
            )
        
        select drug_id, drug_amount
        from critical_amount_drugs
        order by drug_amount
        """
    )

    result = await session.execute(query)

    drugs: list[Drug] = []

    for i in result:
        drug_res = await session.get(DrugOrm, ident=i[0])
        drugs.append(Drug.model_validate(drug_res))

    return drugs


@router.get("/minimal-amount")
async def get_minimal_amount_drugs(drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)) -> list[StoredDrug]:
    tmp = "" if drug_type_id is None else f"where type_id = {drug_type_id}"

    query_s = f"""
        with
            drugs_storage_amount as (
                select
                    drugs.id as drug_id,
                    coalesce(sum(available_amount), 0) as drug_amount,
                    critical_amount
                from drugs
                    left join storage_items on drugs.id = storage_items.drug_id
                {tmp}
                group by
                    drugs.id,
                    critical_amount
            ),
        
            ranked_drugs as (
                select
                  drug_id,
                  dense_rank() over (order by drug_amount) as dr,
                  drug_amount
              from drugs_storage_amount
              group by drug_id
            )
        
        select
            drug_id,
            drug_amount
        from ranked_drugs
        where dr = 1
    """

    query = text(query_s)

    result = await session.execute(query)

    drugs: list[StoredDrug] = []

    for i in result:
        res = await session.get(DrugOrm, ident=i[0])
        drug = Drug.model_validate(res)
        drugs.append(StoredDrug(
            drug=drug,
            stored_count=i[1]
        ))

    return drugs


@router.get("/used")
async def get_used_drugs(period_start: date, period_end: date, session: AsyncSession = Depends(get_session)) -> list[UsedDrug]:
    s1 = f"'{str(period_start).replace('-', '/')}'"
    s2 = f"'{str(period_end).replace('-', '/')}'"

    query = text(
        f"""
            with
                used_in_cooking_drugs as (
                    select
                        component_id as drug_id,
                        sum(component_amount) as drug_amount
                    from production
                        join technology_components on production.technology_id = technology_components.technology_id
                        join drugs on technology_components.component_id = drugs.id
                    where start between {s1} and {s2}
                    group by component_id
                ),
        
                sold_drugs as (
                    select
                        drug_id,
                        sum(amount) as drug_amount
                    from orders
                        join prescriptions_content using (prescription_id)
                    where obtaining_datetime between {s1} and {s2}
                    group by drug_id
                ),
        
                used_drugs as (
                    select
                        drug_id,
                        drugs.name,
                        sum(drug_amount) as drug_amount
                    from (
                        select *
                        from used_in_cooking_drugs
                        union all
                        select *
                        from sold_drugs
                        ) as _
                        join drugs on drug_id = drugs.id
                    group by drug_id)
        
            select drug_id, drug_amount
            from used_drugs
            order by drug_amount desc
        """
    )

    result = await session.execute(query)

    used_drugs: list[UsedDrug] = []

    for i in result:
        d = await session.get(DrugOrm, ident=i[0])
        used_drugs.append(UsedDrug(
            drug=Drug.model_validate(d),
            uses_number=i[1]
        ))

    return used_drugs
