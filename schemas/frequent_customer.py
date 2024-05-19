from pydantic import Field

from .base.base import Base
from .base.customer import Customer


class FrequentCustomer(Base):
    customer: Customer
    order_count: int = Field(ge=0)
