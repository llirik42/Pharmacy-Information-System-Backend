from pydantic import Field

from .base import Base


class DrugType(Base):
    name: str = Field(max_length=256)
    is_cookable: bool = Field(validation_alias='cookable')
