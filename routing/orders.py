from fastapi import APIRouter, Depends
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import OrderOrm
from schemas import Order, CustomerOrder, Prescription, Customer
from schemas.responses import BaseResponse, CreateOrderResponse

router = APIRouter(prefix="/orders")


@router.post("/")
async def create_order(prescription: Prescription) -> CreateOrderResponse:
    return CreateOrderResponse(is_customer_required=True, order_id=0)


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = select(OrderOrm)
    result = await session.execute(query)
    return [Order.model_validate(i) for i in result.unique().scalars().all()]


@router.get("/forgotten")
async def get_forgotten_orders() -> list[CustomerOrder]:
    return []


@router.get("/production")
async def get_orders_in_production(session: AsyncSession = Depends(get_session)) -> list[Order]:
    query = text("select distinct order_id from production")
    result = await session.execute(query)
    print(result.all())
    return []


@router.post("/{order_id}/customers")
async def add_order_customer(order_id: int, customer: Customer) -> BaseResponse:
    return BaseResponse()


@router.post("/{order_id}/pay")
async def add_order_customer() -> BaseResponse:
    return BaseResponse()


@router.post("/{order_id}/obtain")
async def add_order_customer() -> BaseResponse:
    return BaseResponse()
