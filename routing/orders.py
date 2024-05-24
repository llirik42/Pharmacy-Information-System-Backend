import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import (
    Order,
    Customer,
    Doctor,
    Patient,
    Base,
    Drug,
    AdministrationRoute,
)
from schemas import (
    OrderSchema,
    CustomerSchema,
    DoctorSchema,
    PatientSchema,
    DrugSchema,
    AdministrationRouteSchema,
)
from schemas.responses import (
    OrderStatus,
    OrderResponse,
    create_order_not_found_response,
    create_order_internal_error_response,
    create_order_success_response,
)

router = APIRouter(prefix="/orders")
logger = logging.getLogger("orders")


@router.post("/")
async def create_order(prescription_id: int, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    # items: list[PrescriptionItem] = prescription.items
    # drug_orms: list[DrugOrm] = []
    # administration_route_orms: list[AdministrationRouteOrm] = []
    #
    # # Get and validate drugs and administration routes of prescription
    # for it in items:
    #     drug: Drug = it.drug
    #     drug_orm: DrugOrm = await _find_drug(drug=drug, session=session)
    #     if not drug_orm:
    #         message: str = f"Unknown drug {drug.name}"
    #         logger.error(message)
    #         return OrderResponse(
    #             message=message,
    #             status_code=OrderStatus.UNKNOWN_DRUG,
    #         )
    #
    #     administration_route = it.administration_route
    #     administration_route_orm: AdministrationRouteOrm = await _find_administration_route(
    #         administration_route=administration_route,
    #         session=session
    #     )
    #     if not administration_route_orm:
    #         message: str = f"Unknown administration route {administration_route.name}"
    #         logger.error(message)
    #         return OrderResponse(
    #             message=message,
    #             status_code=OrderStatus.UNKNOWN_ADMINISTRATION_ROUTE,
    #         )
    #
    #     drug_orms.append(drug_orm)
    #     administration_route_orms.append(administration_route_orm)
    #
    # # Create prescription
    # doctor_orm: DoctorOrm = await _find_or_create_doctor(doctor=prescription.doctor, session=session)
    # patient_orm: PatientOrm = await _find_or_create_patient(patient=prescription.patient, session=session)
    # prescription_orm = PrescriptionOrm(
    #     diagnosis=prescription.diagnosis,
    #     patient_id=patient_orm.id,
    #     doctor_id=doctor_orm.id,
    #     date=prescription.date,
    # )
    # await _create_object(session=session, obj=prescription_orm)
    #
    # # Add items to prescription
    # for i, it in enumerate(items):
    #     drug_orm = drug_orms[i]
    #     administration_route_orm = administration_route_orms[i]
    #
    #     prescription_item_orm = PrescriptionItemOrm(
    #         prescription_id=prescription_orm.id,
    #         drug_id=drug_orm.id,
    #         amount=it.amount,
    #         administration_route_id=administration_route_orm.id,
    #     )
    #     await _create_object(session=session, obj=prescription_item_orm)
    #
    # # Create order
    # order_orm = OrderOrm(
    #     prescription_id=prescription_orm.id,
    #     registration_datetime=datetime.now(),
    # )
    # await _create_object(session=session, obj=order_orm)
    # await session.commit()
    #
    # # TODO: Add business-logic (reserve drugs, start production)
    # if len(items) > 1:
    #     return OrderResponse(
    #         message="Order waiting drugs", status=OrderStatus.WAITING_PRODUCTION_OR_SUPPLY, order_id=order_orm.id
    #     )

    return OrderResponse(message="Order created", status=OrderStatus.CREATED, order_id=order_orm.id)


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = select(Order)
    query_result = await session.execute(query)
    return [OrderSchema.model_validate(order_orm) for order_orm in query_result.unique().scalars().all()]


@router.get("/forgotten")
async def get_forgotten_orders(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = text(_get_forgotten_orders_query_string())
    query_result = await session.execute(query)

    forgotten_orders: list[OrderSchema] = []

    for row in query_result:
        order_id: int = row[0]
        order_orm = await session.get(Order, ident=order_id)
        forgotten_orders.append(OrderSchema.model_validate(order_orm))

    return forgotten_orders


@router.get("/production")
async def get_orders_in_production(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = text(_get_orders_in_production_query_string())
    query_result = await session.execute(query)

    orders_in_production: list[OrderSchema] = []

    for row in query_result:
        order_id: int = row[0]
        order_orm = await session.get(Order, ident=order_id)
        orders_in_production.append(OrderSchema.model_validate(order_orm))

    return orders_in_production


@router.post("/{order_id}/customers")
async def set_order_customer(
    order_id: int, customer_id: int, session: AsyncSession = Depends(get_session)
) -> OrderResponse:
    # try:
    #     order: Optional[OrderOrm] = await _find_order_by_id(order_id=order_id, session=session)
    # except Exception as e:
    #     logger.error("Searching for order %s failed", order_id, exc_info=e)
    #     return create_order_internal_error_response(
    #         order_id=order_id,
    #     )
    #
    # if order is None:
    #     _log_order_not_found(order_id)
    #     return create_order_not_found_response(order_id)
    #
    # try:
    #     customer_orm: CustomerOrm = await _find_or_create_customer(customer=customer, session=session)
    # except Exception as e:
    #     logger.error(
    #         f"Invalid customer (%s, %s, %s)",
    #         customer.full_name,
    #         customer.phone_number,
    #         customer.address,
    #         exc_info=e
    #     )
    #     return OrderResponse(
    #         message="Invalid customer",
    #         status=OrderStatus.INVALID_CUSTOMER,
    #         order_id=order_id,
    #     )
    #
    # try:
    #     order.customer_id = customer_orm.id
    #     await session.commit()
    #     return create_order_success_response(order_id)
    # except Exception as e:
    #     logger.error(f"Failed to assign customer {customer_orm.id} to order {order_id}", exc_info=e)
    #     return create_order_internal_error_response(
    #         order_id=order_id,
    #     )
    pass


@router.delete("/{order_id}/customers")
async def delete_order_customer(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    try:
        order: Optional[Order] = await _find_order_by_id(order_id=order_id, session=session)
    except Exception as e:
        logger.error("Searching for order %s failed", order_id, exc_info=e)
        return create_order_internal_error_response(
            order_id=order_id,
        )

    if order is None:
        _log_order_not_found(order_id)
        return create_order_not_found_response(order_id)

    if order.customer_id is None:
        logger.error(f"Customer not assigned to order {order_id}")
        return OrderResponse(
            message="Customer not assigned",
            status=OrderStatus.CUSTOMER_NOT_ASSIGNED,
            order_id=order_id
        )

    try:
        order.customer_id = None
        await session.commit()
        return create_order_success_response(order_id)
    except Exception as e:
        logger.error("Failed to delete customer from order %s", order_id, exc_info=e)
        return OrderResponse(
            message="Failed to delete customer",
            order_id=order_id,
            status=OrderStatus.CANNOT_DELETE_CUSTOMER
        )


@router.post("/{order_id}/pay")
async def pay_for_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    try:
        order: Optional[Order] = await _find_order_by_id(order_id=order_id, session=session)
    except Exception as e:
        logger.error("Searching for order %s failed", order_id, exc_info=e)
        return create_order_internal_error_response(
            order_id=order_id,
        )

    if order is None:
        _log_order_not_found(order_id)
        return create_order_not_found_response(order_id)

    if order.paid:
        logger.error(f"Order {order_id} is already paid for")
        return OrderResponse(
            message=f"Order is already paid for",
            status=OrderStatus.ALREADY_PAID,
            order_id=order_id
        )

    try:
        order.paid = True
        await session.commit()
        return create_order_success_response(order_id)
    except Exception as e:
        logger.error("Failed to pay for order %s", order_id, exc_info=e)
        return OrderResponse(
            order_id=order_id,
            message="Order cannot be paid for",
            status=OrderStatus.CANNOT_BE_OBTAINED
        )


@router.post("/{order_id}/obtain")
async def obtain_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderResponse:
    try:
        order: Optional[Order] = await _find_order_by_id(order_id=order_id, session=session)
    except Exception as e:
        logger.error("Searching for order %s failed", order_id, exc_info=e)
        return create_order_internal_error_response(
            order_id=order_id,
        )

    if order is None:
        _log_order_not_found(order_id)
        return create_order_not_found_response(order_id)

    if order.obtaining_datetime is not None:
        logger.error(f"Order {order_id} is already obtained")
        return OrderResponse(
            message=f"Order is already obtained found",
            status=OrderStatus.ALREADY_OBTAINED,
            order_id=order_id
        )

    try:
        order.obtaining_datetime = datetime.now()
        await session.commit()
        return create_order_success_response(order_id)
    except Exception as e:
        logger.error("Failed to obtain order %s", order_id, exc_info=e)
        return OrderResponse(
            order_id=order_id,
            message="Cannot obtain order",
            status=OrderStatus.CANNOT_BE_PAID
        )


async def _find_order_by_id(order_id: int, session: AsyncSession) -> Optional[Order]:
    return await session.get(Order, ident=order_id)


async def _find_or_create_patient(patient: PatientSchema, session: AsyncSession) -> Patient:
    query = select(Patient).where(Patient.full_name == patient.full_name, Patient.birthday == patient.birthday)
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    patient_orm = Patient(
        full_name=patient.full_name,
        birthday=patient.birthday,
    )
    await _create_object(session=session, obj=patient_orm)

    return patient_orm


async def _find_or_create_doctor(doctor: DoctorSchema, session: AsyncSession) -> Doctor:
    query = select(Doctor).where(
        Doctor.full_name == doctor.full_name,
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    doctor_orm = Doctor(
        full_name=doctor.full_name,
    )
    await _create_object(session=session, obj=doctor_orm)

    return doctor_orm


async def _find_or_create_customer(customer: CustomerSchema, session: AsyncSession) -> Customer:
    query = select(Customer).where(
        Customer.full_name == customer.full_name,
        Customer.phone_number == customer.phone_number,
        Customer.address == customer.address,
    )
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    if candidates:
        return candidates[0]

    customer_orm = Customer(
        full_name=customer.full_name,
        phone_number=customer.phone_number,
        address=customer.address,
    )
    await _create_object(session=session, obj=customer_orm)

    return customer_orm


async def _find_drug(drug: DrugSchema, session: AsyncSession) -> Optional[Drug]:
    query = select(Drug).where(Drug.name == drug.name)
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    return candidates[0] if candidates else None


async def _find_administration_route(
    administration_route: AdministrationRouteSchema, session: AsyncSession
) -> Optional[AdministrationRoute]:
    query = select(AdministrationRoute).where(AdministrationRoute.description == administration_route.description)
    query_result = await session.execute(query)
    candidates = query_result.scalars().all()

    return candidates[0] if candidates else None




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


def _log_order_not_found(order_id: int) -> None:
    logger.error(f"Order {order_id} not found")
