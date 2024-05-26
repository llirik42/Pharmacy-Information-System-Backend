import logging

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Doctor
from schemas import DoctorSchema, InputDoctorSchema
from .doctor_creation_response import DoctorCreationResponseSchema
from .doctor_creation_status import DoctorCreationStatus
from ..utils import create_object

router = APIRouter(prefix="/doctors")
logger = logging.getLogger("doctors")


@router.get("/")
async def get_doctors(session: AsyncSession = Depends(get_session)) -> list[DoctorSchema]:
    query = select(Doctor)
    query_result = await session.execute(query)
    return [DoctorSchema.model_validate(doctor_orm) for doctor_orm in query_result.scalars().all()]


@router.post("/")
async def create_doctor(
    input_doctor: InputDoctorSchema, session: AsyncSession = Depends(get_session)
) -> DoctorCreationResponseSchema:
    try:
        doctor = Doctor(full_name=input_doctor.full_name)
        await create_object(session, doctor)
        await session.commit()
        return DoctorCreationResponseSchema(status=DoctorCreationStatus.SUCCESS)
    except IntegrityError as e:
        logger.error(f"Creation of ({input_doctor}) failed", exc_info=e)
        return DoctorCreationResponseSchema(status=DoctorCreationStatus.ALREADY_EXISTS)
