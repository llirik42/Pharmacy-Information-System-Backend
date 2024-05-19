from pydantic import Field

from .order_status import OrderStatus
from ..base.base import Base


class OrderResponse(Base):
    message: str
    status: OrderStatus = Field(
        description="".join([f"{i} - {OrderStatus(i).name}, " for i in range(len(OrderStatus))])
    )
    order_id: int = 0


def create_order_success_response(order_id: int) -> OrderResponse:
    return OrderResponse(message="Success", status=OrderStatus.SUCCESS, order_id=order_id)


def create_order_not_found_response(order_id: int) -> OrderResponse:
    return OrderResponse(message=f"Order not found", status=OrderStatus.NOT_FOUND, order_id=order_id)


def create_order_internal_error_response(order_id: int) -> OrderResponse:
    return OrderResponse(status=OrderStatus.INTERNAL_ERROR, order_id=order_id)
