from pydantic import Field

from ..input import InputCustomerSchema


class CustomerSchema(InputCustomerSchema):
    id: int = Field(ge=1)
