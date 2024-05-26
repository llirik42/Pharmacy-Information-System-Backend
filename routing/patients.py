from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Patient
from schemas.entities import PatientSchema

router = APIRouter(prefix="/patients")


@router.get("/")
async def get_patients(session: AsyncSession = Depends(get_session)) -> list[PatientSchema]:
    query = select(Patient)
    query_result = await session.execute(query)
    return [PatientSchema.model_validate(patient) for patient in query_result.scalars().all()]
