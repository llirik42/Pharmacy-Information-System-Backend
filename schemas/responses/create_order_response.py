from .base_response import BaseResponse


class CreateOrderResponse(BaseResponse):
    is_customer_required: bool = False
    order_id: int = 0


def create_error_order_response(message: str) -> CreateOrderResponse:
    return CreateOrderResponse(is_successs=False, message=message)
