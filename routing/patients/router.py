import logging
from typing import Optional

from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Patient
from schemas import PatientSchema, InputPatientSchema
from .patient_creation_response import PatientCreationResponseSchema
from .patient_creation_status import PatientCreationStatus
from .patient_search_response import PatientSearchResponseSchema
from ..utils import create_object

router = APIRouter(prefix="/patients")
logger = logging.getLogger("patients")


@router.get("/")
async def get_patients(session: AsyncSession = Depends(get_session)) -> list[PatientSchema]:
    query = select(Patient)
    query_result = await session.execute(query)
    return [PatientSchema.model_validate(patient) for patient in query_result.scalars().all()]


@router.get("/search")
async def find_patient(patient_id: int, session: AsyncSession = Depends(get_session)) -> PatientSearchResponseSchema:
    optional_patient: Optional[Patient] = await session.get(Patient, ident=patient_id)
    return PatientSearchResponseSchema(patient=optional_patient)


@router.post("/")
async def create_patient(
    input_patient: InputPatientSchema, session: AsyncSession = Depends(get_session)
) -> PatientCreationResponseSchema:
    try:
        patient = Patient(full_name=input_patient.full_name, birthday=input_patient.birthday)
        await create_object(session, patient)
        await session.commit()
        return PatientCreationResponseSchema(status=PatientCreationStatus.SUCCESS)
    except Exception as e:
        logger.error(f"Creation of ({input_patient}) failed", exc_info=e)
        return PatientCreationResponseSchema(status=PatientCreationStatus.ALREADY_EXISTS)
