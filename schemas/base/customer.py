from pydantic import Field

from .base import Base


class Customer(Base):
    id: int = Field(ge=1)
    full_name: str = Field(max_length=256)
    phone_number: str = Field(max_length=32)
    address: str = Field(max_length=256)
