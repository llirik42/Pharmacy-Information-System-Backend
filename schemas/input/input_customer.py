from pydantic import Field

from ..base import BaseSchema


class InputCustomerSchema(BaseSchema):
    full_name: str = Field(max_length=256)
    phone_number: str = Field(max_length=32)
    address: str = Field(max_length=256)
