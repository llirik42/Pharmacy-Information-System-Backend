from pydantic import Field

from .base.customer import Customer


class FrequentCustomer(Customer):
    orders_count: int = Field(ge=0)
