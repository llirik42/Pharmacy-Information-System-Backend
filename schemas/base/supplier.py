from pydantic import Field

from .base import Base


class Supplier(Base):
    id: int = Field(ge=1)
    name: str = Field(max_length=256)
    phone_number: str = Field(max_length=32)
