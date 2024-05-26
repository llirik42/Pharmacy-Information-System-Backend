from pydantic import Field

from .base.base import BaseSchema
from .base.customer import CustomerSchema


class FrequentCustomerSchema(BaseSchema):
    customer: CustomerSchema
    order_count: int = Field(ge=0)
