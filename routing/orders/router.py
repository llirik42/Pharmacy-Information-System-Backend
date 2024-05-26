import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import (
    Order,
)
from schemas import OrderSchema, InputOrderSchema
from .order_creation_response import OrderCreationResponseSchema
from .order_creation_status import OrderCreationStatus
from .order_obtain_response import OrderObtainResponseSchema
from .order_obtain_status import OrderObtainStatus
from .order_payment_response import OrderPaymentResponseSchema
from .order_payment_status import OrderPaymentStatus
from .order_search_response import OrderSearchResponseSchema
from ..utils import create_object

router = APIRouter(prefix="/orders")
logger = logging.getLogger("orders")


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = select(Order)
    query_result = await session.execute(query)
    return [OrderSchema.model_validate(o) for o in query_result.unique().scalars().all()]


@router.get("/search")
async def find_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderSearchResponseSchema:
    optional_order: Optional[Order] = await session.get(Order, ident=order_id)
    return OrderSearchResponseSchema(order=optional_order)


@router.post("/")
async def create_order(
    input_order: InputOrderSchema, session: AsyncSession = Depends(get_session)
) -> OrderCreationResponseSchema:
    try:
        order = Order(
            prescription_id=input_order.prescription_id,
            registration_datetime=datetime.now(),
            customer_id=input_order.customer_id,
        )
        await create_object(session, order)
        await session.commit()
        return OrderCreationResponseSchema(status=OrderCreationStatus.SUCCESS, order_id=order.id)
    except Exception as e:
        logger.error(f"Creation of ({input_order}) failed", exc_info=e)
        return OrderCreationResponseSchema(status=OrderCreationStatus.INVALID)


@router.get("/forgotten")
async def get_forgotten_orders(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = text(_get_forgotten_orders_query_string())
    query_result = await session.execute(query)

    forgotten_orders: list[OrderSchema] = []

    for row in query_result:
        order_id: int = row[0]
        order = await session.get(Order, ident=order_id)
        forgotten_orders.append(OrderSchema.model_validate(order))

    return forgotten_orders


@router.get("/production")
async def get_orders_in_production(session: AsyncSession = Depends(get_session)) -> list[OrderSchema]:
    query = text(_get_orders_in_production_query_string())
    query_result = await session.execute(query)

    orders_in_production: list[OrderSchema] = []

    for row in query_result:
        order_id: int = row[0]
        order = await session.get(Order, ident=order_id)
        orders_in_production.append(OrderSchema.model_validate(order))

    return orders_in_production


@router.post("/{order_id}/payment")
async def pay_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderPaymentResponseSchema:
    order: Optional[Order] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        return OrderPaymentResponseSchema(status=OrderPaymentStatus.NOT_FOUND)

    if order.paid:
        logger.error(f"Failed to pay for order {order_id}, because it's paid for")
        return OrderPaymentResponseSchema(status=OrderPaymentStatus.ALREADY_PAID)

    try:
        order.paid = True
        await session.commit()
        return OrderPaymentResponseSchema(status=OrderPaymentStatus.SUCCESS)
    except Exception as e:
        logger.error("Failed to pay for order %s", order_id, exc_info=e)
        return OrderPaymentResponseSchema(status=OrderPaymentStatus.CANNOT_BE_PAID)


@router.post("/{order_id}/obtain")
async def obtain_order(order_id: int, session: AsyncSession = Depends(get_session)) -> OrderObtainResponseSchema:
    order: Optional[Order] = await _find_order_by_id(order_id=order_id, session=session)

    if order is None:
        return OrderObtainResponseSchema(status=OrderObtainStatus.NOT_FOUND)

    if order.obtaining_datetime is not None:
        logger.error(f"Failed to obtain order {order_id}, because it's already obtained")
        return OrderObtainResponseSchema(status=OrderObtainStatus.ALREADY_OBTAINED)

    try:
        order.obtaining_datetime = datetime.now()
        await session.commit()
        return OrderObtainResponseSchema(status=OrderObtainStatus.SUCCESS)
    except Exception as e:
        logger.error("Failed to obtain order %s", order_id, exc_info=e)
        return OrderObtainResponseSchema(status=OrderObtainStatus.CANNOT_BE_OBTAINED)


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


async def _find_order_by_id(order_id: int, session: AsyncSession) -> Optional[Order]:
    return await session.get(Order, ident=order_id)
