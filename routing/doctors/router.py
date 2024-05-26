from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Doctor
from schemas import DoctorSchema

router = APIRouter(prefix="/doctors")


@router.get("/")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[DoctorSchema]:
    query = select(Doctor)
    query_result = await session.execute(query)
    return [DoctorSchema.model_validate(doctor_orm) for doctor_orm in query_result.scalars().all()]
