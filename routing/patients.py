import logging
from datetime import datetime

from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import PatientOrm
from schemas import Patient

router = APIRouter(prefix="/patients")
logger = logging.getLogger("patients")


@router.post("/")
async def create_patient(full_name: str, birthday: datetime, session: AsyncSession = Depends(get_session)):
    pass


@router.get("/")
async def get_patients(session: AsyncSession = Depends(get_session)) -> list[Patient]:
    query = select(PatientOrm)
    query_result = await session.execute(query)
    return [Patient.model_validate(p) for p in query_result.scalars().all()]
