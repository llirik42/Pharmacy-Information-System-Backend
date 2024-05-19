import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import (
    OrderOrm,
    CustomerOrm,
    DoctorOrm,
    PatientOrm,
    PrescriptionOrm,
    PrescriptionItemOrm,
    Base,
    DrugOrm,
    AdministrationRouteOrm,
)
from schemas import (
    Order,
    Prescription,
    Customer,
    Doctor,
    Patient,
    Drug,
    AdministrationRoute,
    PrescriptionItem,
)
from schemas.responses import (
    BaseResponse,
    CreateOrderResponse,
    create_error_base_response,
    create_error_order_response
)

router = APIRouter(prefix="/orders")
logger = logging.getLogger("orders")


@router.post("/")
async def create_order(
        prescription: Prescription,
        session: AsyncSession = Depends(get_session)
) -> CreateOrderResponse:
    items: list[PrescriptionItem] = prescription.items
    drug_orms: list[DrugOrm] = []
    administration_route_orms: list[AdministrationRouteOrm] = []

    # Get and validate drugs and administration routes of prescription
    for it in items:
        drug: Drug = it.drug
        drug_orm: DrugOrm = await _find_drug(drug=drug, session=session)
        if not drug_orm:
            message: str = f"Unknown drug {drug.name}"
            logger.error(message)
            return create_error_order_response(message)

        administration_route = it.administration_route
        administration_route_orm: AdministrationRouteOrm = await _find_administration_route(
            administration_route=administration_route, session=session
        )
        if not administration_route_orm:
            message: str = f"Unknown administration route {administration_route.name}"
            logger.error(message)
            return create_error_order_response(message)

        drug_orms.append(drug_orm)
        administration_route_orms.append(administration_route_orm)

    # Create prescription
    doctor_orm: DoctorOrm = await _find_or_create_doctor(doctor=prescription.doctor, session=session)
    patient_orm: PatientOrm = await _find_or_create_patient(patient=prescription.patient, session=session)
    prescription_orm = PrescriptionOrm(
        diagnosis=prescription.diagnosis,
        patient_id=patient_orm.id,
        doctor_id=doctor_orm.id,
        date=prescription.date,
    )
    await _create_object(session=session, obj=prescription_orm)

    # Add items to prescription
    for i, it in enumerate(items):
        drug_orm = drug_orms[i]
        administration_route_orm = administration_route_orms[i]

        prescription_item_orm = PrescriptionItemOrm(
            prescription_id=prescription_orm.id,
            drug_id=drug_orm.id,
            amount=it.amount,
            administration_route_id=administration_route_orm.id,
        )
        await _create_object(session=session, obj=prescription_item_orm)

    # Create order
    order_orm = OrderOrm(
        prescription_id=prescription_orm.id,
        registration_datetime=datetime.now(),
    )
    await _create_object(session=session, obj=order_orm)

    await session.commit()

    # TODO: add business-logic: reserving drugs, starting production etc.
    return CreateOrderResponse(is_customer_required=True, order_id=order_orm.id)


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = select(OrderOrm)
    query_result = await session.execute(query)
    return [Order.model_validate(order_orm) for order_orm in query_result.unique().scalars().all()]


@router.get("/forgotten")
async def get_forgotten_orders(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = text(_get_forgotten_orders_query_string())
    query_result = await session.execute(query)

    forgotten_orders: list[Order] = []

    for row in query_result:
        order_id: int = row[0]
        order_orm = await session.get(OrderOrm, ident=order_id)
        forgotten_orders.append(Order.model_validate(order_orm))

    return forgotten_orders


@router.get("/production")
async def get_orders_in_production(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = text(_get_orders_in_production_query_string())
    query_result = await session.execute(query)

    orders_in_production: list[Order] = []

    for row in query_result:
        order_id: int = row[0]
        order_orm = await session.get(OrderOrm, ident=order_id)
        orders_in_production.append(Order.model_validate(order_orm))

    return orders_in_production


@router.post("/{order_id}/customers")
async def set_order_customer(
    order_id: int, customer: Customer, session: AsyncSession = Depends(get_session)
) -> BaseResponse:
    order: Optional[OrderOrm] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        message: str = f"Order {order_id} not found"
        logger.error(message)
        return create_error_base_response(message)

    customer_orm: CustomerOrm = await _find_or_create_customer(customer=customer, session=session)

    try:
        order.customer_id = customer_orm.id
        await session.commit()
        return BaseResponse()
    except Exception as e:
        message: str = f"Failed to assign customer {customer_orm.id} for order {order_id}"
        logger.error(message, exc_info=e)
        return create_error_base_response(message)


@router.delete("/{order_id}/customers")
async def delete_order_customer(order_id: int, session: AsyncSession = Depends(get_session)) -> BaseResponse:
    order: Optional[OrderOrm] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        message: str = f"Order {order_id} not found"
        logger.error(message)
        return create_error_base_response(message)

    try:
        order.customer_id = None
        await session.commit()
        return BaseResponse()
    except Exception as e:
        message: str = f"Failed to remove customer from order {order_id}"
        logger.error(message, exc_info=e)
        return create_error_base_response(message)


@router.post("/{order_id}/pay")
async def pay_for_order(order_id: int, session: AsyncSession = Depends(get_session)) -> BaseResponse:
    order: Optional[OrderOrm] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        message: str = f"Order {order_id} not found"
        logger.error(message)
        return create_error_base_response(message)

    if order.paid:
        message: str = f"Order {order_id} has already been paid for"
        logger.error(message)
        return create_error_base_response(message)

    try:
        order.paid = True
        await session.commit()
        return BaseResponse()
    except Exception as e:
        message: str = f"Failed to pay for order {order_id}"
        logger.error(message, exc_info=e)
        return create_error_base_response(message)


@router.post("/{order_id}/obtain")
async def obtain_order(order_id: int, session: AsyncSession = Depends(get_session)) -> BaseResponse:
    order: Optional[OrderOrm] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        message: str = f"Order {order_id} not found"
        logger.error(message)
        return create_error_base_response(message)

    if order.obtaining_datetime is not None:
        message: str = f"Order {order_id} has already been obtained"
        logger.error(message)
        return create_error_base_response(message)

    try:
        order.obtaining_datetime = datetime.now()
        await session.commit()
        return BaseResponse()
    except Exception as e:
        message: str = f"Failed to obtain order {order_id}"
        logger.error(message, exc_info=e)
        return create_error_base_response(message)


async def _find_order_by_id(order_id: int, session: AsyncSession) -> Optional[OrderOrm]:
    return await session.get(OrderOrm, ident=order_id)


async def _find_or_create_patient(patient: Patient, session: AsyncSession) -> PatientOrm:
    query = select(PatientOrm).where(
        PatientOrm.full_name == patient.full_name,
        PatientOrm.birthday == patient.birthday
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    patient_orm = PatientOrm(
        full_name=patient.full_name,
        birthday=patient.birthday,
    )
    await _create_object(session=session, obj=patient_orm)

    return patient_orm


async def _find_or_create_doctor(doctor: Doctor, session: AsyncSession) -> DoctorOrm:
    query = select(DoctorOrm).where(
        DoctorOrm.full_name == doctor.full_name,
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    doctor_orm = DoctorOrm(
        full_name=doctor.full_name,
    )
    await _create_object(session=session, obj=doctor_orm)

    return doctor_orm


async def _find_or_create_customer(customer: Customer, session: AsyncSession) -> CustomerOrm:
    query = select(CustomerOrm).where(
        CustomerOrm.full_name == customer.full_name,
        CustomerOrm.phone_number == customer.phone_number,
        CustomerOrm.address == customer.address,
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    customer_orm = CustomerOrm(
        full_name=customer.full_name,
        phone_number=customer.phone_number,
        address=customer.address,
    )
    await _create_object(session=session, obj=customer_orm)

    return customer_orm


async def _find_drug(drug: Drug, session: AsyncSession) -> Optional[DrugOrm]:
    query = select(DrugOrm).where(DrugOrm.name == drug.name)
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    return candidates[0] if candidates else None


async def _find_administration_route(
    administration_route: AdministrationRoute, session: AsyncSession
) -> Optional[AdministrationRouteOrm]:
    query = select(AdministrationRouteOrm).where(
        AdministrationRouteOrm.description == administration_route.description
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    return candidates[0] if candidates else None


async def _create_object(session: AsyncSession, obj: Base) -> None:
    session.add(obj)
    await session.flush()
    await session.refresh(obj)


def _get_forgotten_orders_query_string() -> str:
    return """
        select distinct
            id as order_id
        from orders
        where
            appointed_datetime is not null
            and appointed_datetime <= now()
            and (
                obtaining_datetime is null
                or obtaining_datetime <> appointed_datetime
            )
    """


def _get_orders_in_production_query_string() -> str:
    return """
        select distinct order_id from production
    """
