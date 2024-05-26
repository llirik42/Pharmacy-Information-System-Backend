from schemas import BaseSchema

from .order_creation_status import OrderCreationStatus


class OrderCreationResponseSchema(BaseSchema):
    status: OrderCreationStatus
