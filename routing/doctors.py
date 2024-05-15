from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DoctorOrm
from schemas import Doctor

router = APIRouter(prefix="/doctors")


@router.get("/")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[Doctor]:
    query = select(DoctorOrm)
    result = await session.execute(query)
    return [Doctor.model_validate(i) for i in result.scalars().all()]
