from schemas import BaseSchema
from .order_payment_status import OrderPaymentStatus


class OrderPaymentResponseSchema(BaseSchema):
    status: OrderPaymentStatus
