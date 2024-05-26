from pydantic import Field

from schemas import BaseSchema
from .order_creation_status import OrderCreationStatus


class OrderCreationResponseSchema(BaseSchema):
    status: OrderCreationStatus
    order_id: int = Field(ge=1, default=0)
