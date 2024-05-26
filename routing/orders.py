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
from schemas.entities import (
    OrderSchema,
)
from schemas.responses import (
    OrderObtainStatus,
    OrderPaymentStatus,
    OrderObtainResponseSchema,
    OrderPaymentResponseSchema,
)

router = APIRouter(prefix="/orders")
logger = logging.getLogger("routing.orders")


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
