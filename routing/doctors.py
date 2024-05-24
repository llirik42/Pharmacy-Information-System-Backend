import logging
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Doctor
from routing.utils import create_object
from schemas import DoctorSchema
from schemas.responses.doctor import DoctorResponse, DoctorResponseStatus

router = APIRouter(prefix="/doctors")
logger = logging.getLogger("doctors")


@router.post("/")
async def create_doctor(full_name: str, session: AsyncSession = Depends(get_session)) -> DoctorResponse:
    doctor_orm = Doctor(full_name=full_name)

    try:
        await create_object(obj=doctor_orm, session=session)
        return DoctorResponse(
            doctor=DoctorSchema.model_validate(doctor_orm)
        )
    except Exception as e:
        logger.error("Creating customer (%s) failed", full_name, exc_info=e)
        return DoctorResponse(
            status=DoctorResponseStatus.INVALID
        )


@router.get("/")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[DoctorSchema]:
    query = select(Doctor)
    query_result = await session.execute(query)
    return [DoctorSchema.model_validate(doctor_orm) for doctor_orm in query_result.scalars().all()]


@router.get("/")
async def find_doctor(doctor_id: int, session: AsyncSession = Depends(get_session)) -> DoctorResponse:
    doctor_orm: Optional[Doctor] = await session.get(Doctor, ident=doctor_id)

    if doctor_orm is None:
        logger.error("Doctor %s not found", doctor_id)
        return DoctorResponse(
            status=DoctorResponseStatus.NOT_FOUND,
        )

    return DoctorResponse(
        doctor=DoctorSchema.model_validate(doctor_orm)
    )
