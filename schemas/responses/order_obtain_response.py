from .order_obtain_status import OrderObtainStatus
from ..entities import BaseSchema


class OrderObtainResponseSchema(BaseSchema):
    status: OrderObtainStatus
