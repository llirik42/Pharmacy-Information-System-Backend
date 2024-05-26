import logging
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Prescription, PrescriptionItem
from schemas import PrescriptionSchema, InputPrescriptionSchema, InputPrescriptionItemSchema
from .prescription_creation_response import PrescriptionCreationResponseSchema
from .prescription_creation_status import PrescriptionCreationStatus
from .prescription_search_response import PrescriptionSearchResponseSchema
from ..utils import create_object

router = APIRouter(prefix="/prescriptions")
logger = logging.getLogger("prescriptions")


@router.get("/")
async def get_prescriptions(session: AsyncSession = Depends(get_session)) -> list[PrescriptionSchema]:
    query = select(Prescription)
    query_result = await session.execute(query)
    return [PrescriptionSchema.model_validate(doctor_orm) for doctor_orm in query_result.scalars().unique().all()]


@router.get("/search")
async def find_prescription(
    prescription_id: int, session: AsyncSession = Depends(get_session)
) -> PrescriptionSearchResponseSchema:
    optional_prescription: Optional[Prescription] = await session.get(Prescription, ident=prescription_id)
    return PrescriptionSearchResponseSchema(prescription=optional_prescription)


@router.post("/")
async def create_prescription(
    input_prescription: InputPrescriptionSchema, session: AsyncSession = Depends(get_session)
) -> PrescriptionCreationResponseSchema:
    try:
        prescription = Prescription(
            diagnosis=input_prescription.diagnosis,
            patient_id=input_prescription.patient_id,
            doctor_id=input_prescription.doctor_id,
            date=input_prescription.date,
        )
        await create_object(session, prescription)
    except Exception as e:
        logger.error(f"Creation of ({input_prescription}) (without items) failed", exc_info=e)
        return PrescriptionCreationResponseSchema(status=PrescriptionCreationStatus.INVALID)

    try:
        items: list[InputPrescriptionItemSchema] = input_prescription.items

        for it in items:
            prescription_item = PrescriptionItem(
                prescription_id=prescription.id,
                drug_id=it.drug_id,
                amount=it.amount,
                administration_route_id=it.administration_route_id,
            )
            session.add(prescription_item)

        await session.flush()
        await session.commit()
        return PrescriptionCreationResponseSchema(status=PrescriptionCreationStatus.SUCCESS)
    except Exception as e:
        logger.error(f"Adding items of ({prescription}) failed", exc_info=e)
        return PrescriptionCreationResponseSchema(status=PrescriptionCreationStatus.INVALID)
