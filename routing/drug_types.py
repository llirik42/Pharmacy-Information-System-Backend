from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugTypeOrm
from schemas import DrugType

router = APIRouter(prefix="/drug-types")


@router.get("/")
async def get_drug_types(session: AsyncSession = Depends(get_session)) -> list[DrugType]:
    query = select(DrugTypeOrm)
    result = await session.execute(query)
    return [DrugType.model_validate(i) for i in result.scalars().all()]


@router.get("/critical-amount")
async def get_critical_amount_drug_types(session: AsyncSession = Depends(get_session)) -> list[DrugType]:
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
        
        select distinct
            type_id
        from critical_amount_drugs
            join drugs on critical_amount_drugs.drug_id = drugs.id
        order by
            type_id
        """
    )

    result = await session.execute(query)

    drug_types: list[DrugType] = []

    for i in result:
        drug_type_res = await session.get(DrugTypeOrm, ident=i[0])
        drug_types.append(DrugType.model_validate(drug_type_res))

    return drug_types
