from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugOrm
from schemas import StoredDrug, UsedDrug, Drug
from .utils import date_to_mysql_string

router = APIRouter(prefix="/drugs")


@router.get("/")
async def get_drugs(session: AsyncSession = Depends(get_session)) -> list[Drug]:
    query = select(DrugOrm)
    query_result = await session.execute(query)
    return [Drug.model_validate(drug_orm) for drug_orm in query_result.scalars().all()]


@router.get("/popular")
async def get_popular_drugs(
    limit: int = 10, drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> list[UsedDrug]:
    query = text(_get_popular_drugs_query_string(drug_type_id=drug_type_id, limit=limit))
    query_result = await session.execute(query)

    popular_drugs: list[UsedDrug] = []

    for row in query_result:
        drug_id: int = row[0]
        drug_orm = await session.get(DrugOrm, ident=drug_id)
        popular_drugs.append(UsedDrug(drug=Drug.model_validate(drug_orm), use_number=row[1]))

    return popular_drugs


@router.get("/critical-amount")
async def get_critical_amount_drugs(session: AsyncSession = Depends(get_session)) -> list[Drug]:
    query = text(_get_critical_amount_drugs_query_string())
    query_result = await session.execute(query)

    critical_amount_drugs: list[Drug] = []

    for row in query_result:
        drug_id: int = row[0]
        drug_orm = await session.get(DrugOrm, ident=drug_id)
        critical_amount_drugs.append(Drug.model_validate(drug_orm))

    return critical_amount_drugs


@router.get("/minimal-amount")
async def get_minimal_amount_drugs(
    drug_type_id: Optional[int] = None, session: AsyncSession = Depends(get_session)
) -> list[StoredDrug]:
    query = text(_get_minimal_amount_drugs_query_string(drug_type_id))
    query_result = await session.execute(query)

    minimal_amount_drugs: list[StoredDrug] = []

    for row in query_result:
        drug_id: int = row[0]
        drug_orm = await session.get(DrugOrm, ident=drug_id)
        minimal_amount_drugs.append(StoredDrug(drug=Drug.model_validate(drug_orm), stored_number=row[1]))

    return minimal_amount_drugs


@router.get("/used")
async def get_used_drugs(
    period_start: date, period_end: date, session: AsyncSession = Depends(get_session)
) -> list[UsedDrug]:
    query = text(_get_used_drugs_query_string(period_start=period_start, period_end=period_end))
    query_result = await session.execute(query)

    used_drugs: list[UsedDrug] = []

    for row in query_result:
        drug_id: int = row[0]
        drug_orm = await session.get(DrugOrm, ident=drug_id)
        used_drugs.append(UsedDrug(drug=Drug.model_validate(drug_orm), use_number=row[1]))

    return used_drugs


def _get_popular_drugs_query_string(drug_type_id: Optional[int], limit: int) -> str:
    condition: str = "" if drug_type_id is None else f"where type_id = {drug_type_id}"

    return f"""
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
                {condition}
                group by drug_id)
                
        select drug_id, drug_amount
        from used_drugs
        order by drug_amount desc
        limit {limit}
    """


def _get_critical_amount_drugs_query_string() -> str:
    return """
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


def _get_minimal_amount_drugs_query_string(drug_type_id: Optional[int]) -> str:
    condition: str = "" if drug_type_id is None else f"where type_id = {drug_type_id}"

    return f"""
        with
            drugs_storage_amount as (
                select
                    drugs.id as drug_id,
                    coalesce(sum(available_amount), 0) as drug_amount,
                    critical_amount
                from drugs
                    left join storage_items on drugs.id = storage_items.drug_id
                {condition}
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


def _get_used_drugs_query_string(period_start: date, period_end: date) -> str:
    period_start_string: str = date_to_mysql_string(period_start)
    period_end_string: str = date_to_mysql_string(period_end)

    return f"""
            with
                used_in_cooking_drugs as (
                    select
                        component_id as drug_id,
                        sum(component_amount) as drug_amount
                    from production
                        join technology_components on production.technology_id = technology_components.technology_id
                        join drugs on technology_components.component_id = drugs.id
                    where start between {period_start_string} and {period_end_string}
                    group by component_id
                ),
        
                sold_drugs as (
                    select
                        drug_id,
                        sum(amount) as drug_amount
                    from orders
                        join prescriptions_content using (prescription_id)
                    where obtaining_datetime between {period_start_string} and {period_end_string}
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
