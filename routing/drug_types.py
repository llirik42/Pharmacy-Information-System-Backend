from fastapi import APIRouter, Depends
from sqlalchemy import select
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
async def get_critical_amount_drug_types() -> list[DrugType]:
    return []
