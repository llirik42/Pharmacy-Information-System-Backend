from .order_payment_status import OrderPaymentStatus
from ..entities import BaseSchema


class OrderPaymentResponseSchema(BaseSchema):
    status: OrderPaymentStatus
