from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import PatientOrm
from schemas import Patient

router = APIRouter(prefix="/patients")


@router.get("/")
async def get_patients(session: AsyncSession = Depends(get_session)) -> list[Patient]:
    query = select(PatientOrm)
    result = await session.execute(query)
    return [Patient.model_validate(i) for i in result.scalars().all()]
