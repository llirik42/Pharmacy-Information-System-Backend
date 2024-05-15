from .base_response import BaseResponse


class CreateOrderResponse(BaseResponse):
    is_customer_required: bool
    order_id: int
