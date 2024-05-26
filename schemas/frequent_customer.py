from pydantic import Field

from .base import BaseSchema
from .entities import CustomerSchema


class FrequentCustomerSchema(BaseSchema):
    customer: CustomerSchema
    order_count: int = Field(ge=0)
