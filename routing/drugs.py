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
async def get_popular_drugs(limit: int = 10, drug_type_id: Optional[int] = None) -> list[UsedDrug]:
    return []


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
async def get_minimal_amount_drugs(drug_type_id: Optional[int] = None) -> list[StoredDrug]:
    return []


@router.get("/used")
async def get_used_drugs(period_start: date, period_end: date) -> list[UsedDrug]:
    return []
