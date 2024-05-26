from fastapi import APIRouter, Depends
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugType
from schemas import DrugTypeSchema

router = APIRouter(prefix="/drug-types")


@router.get("/")
async def get_drug_types(session: AsyncSession = Depends(get_session)) -> list[DrugTypeSchema]:
    query = select(DrugType)
    query_result = await session.execute(query)
    return [DrugTypeSchema.model_validate(drug_type_orm) for drug_type_orm in query_result.scalars().all()]


@router.get("/critical-amount")
async def get_critical_amount_drug_types(session: AsyncSession = Depends(get_session)) -> list[DrugTypeSchema]:
    query = text(_get_critical_amount_drug_types_query_string())
    query_result = await session.execute(query)

    critical_amount_drug_types: list[DrugTypeSchema] = []

    for row in query_result:
        drug_type_id: int = row[0]
        drug_type_orm = await session.get(DrugType, ident=drug_type_id)
        critical_amount_drug_types.append(DrugTypeSchema.model_validate(drug_type_orm))

    return critical_amount_drug_types


def _get_critical_amount_drug_types_query_string() -> str:
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
        
        select distinct
            type_id
        from critical_amount_drugs
            join drugs on critical_amount_drugs.drug_id = drugs.id
        order by
            type_id
    """
