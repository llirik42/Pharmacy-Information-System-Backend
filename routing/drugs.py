from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
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
async def get_critical_amount_drugs() -> list[Drug]:
    return []


@router.get("/minimal-amount")
async def get_minimal_amount_drugs(drug_type_id: Optional[int] = None) -> list[StoredDrug]:
    return []


@router.get("/used")
async def get_used_drugs(period_start: date, period_end: date) -> list[UsedDrug]:
    return []
