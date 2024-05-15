from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import CustomerOrm
from schemas import Customer, FrequentCustomer

router = APIRouter(prefix="/customers")


@router.get("/")
async def get_customers(session: AsyncSession = Depends(get_session)) -> list[Customer]:
    query = select(CustomerOrm)
    result = await session.execute(query)
    return [Customer.model_validate(i) for i in result.scalars().all()]


@router.get("/waiting-supplies")
async def get_waiting_supplies_customers(drug_type_id: Optional[int] = None) -> list[Customer]:
    return []


@router.get("/ordered-something")
async def get_ordered_something_customers(
    period_start: date, period_end: date, drug_id: Optional[int] = None, drug_type_id: Optional[int] = None
) -> list[Customer]:
    return []


@router.get("/frequent")
async def get_frequent_customers(
    drug_id: Optional[int] = None, drug_type_id: Optional[int] = None
) -> list[FrequentCustomer]:
    return []
