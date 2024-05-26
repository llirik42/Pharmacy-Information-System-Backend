import logging
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Doctor
from schemas import DoctorSchema, InputDoctorSchema
from .doctor_creation_response import DoctorCreationResponseSchema
from .doctor_creation_status import DoctorCreationStatus
from .doctor_search_response import DoctorSearchResponseSchema
from ..utils import create_object

router = APIRouter(prefix="/doctors")
logger = logging.getLogger("doctors")


@router.get("/")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[DoctorSchema]:
    query = select(Doctor)
    query_result = await session.execute(query)
    return [DoctorSchema.model_validate(d) for d in query_result.scalars().all()]


@router.get("/search")
async def find_doctor(doctor_id: int, session: AsyncSession = Depends(get_session)) -> DoctorSearchResponseSchema:
    optional_doctor: Optional[Doctor] = await session.get(Doctor, ident=doctor_id)
    return DoctorSearchResponseSchema(doctor=optional_doctor)


@router.post("/")
async def create_doctor(
    input_doctor: InputDoctorSchema, session: AsyncSession = Depends(get_session)
) -> DoctorCreationResponseSchema:
    try:
        doctor = Doctor(full_name=input_doctor.full_name)
        await create_object(session, doctor)
        await session.commit()
        return DoctorCreationResponseSchema(status=DoctorCreationStatus.SUCCESS, doctor_id=doctor.id)
    except Exception as e:
        logger.error(f"Creation of ({input_doctor}) failed", exc_info=e)
        return DoctorCreationResponseSchema(status=DoctorCreationStatus.ALREADY_EXISTS)
