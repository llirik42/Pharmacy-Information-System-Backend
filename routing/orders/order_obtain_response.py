from schemas import BaseSchema
from .order_obtain_status import OrderObtainStatus


class OrderObtainResponseSchema(BaseSchema):
    status: OrderObtainStatus
