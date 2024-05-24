import logging

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

router = APIRouter(prefix="/orders")
logger = logging.getLogger("orders")


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
