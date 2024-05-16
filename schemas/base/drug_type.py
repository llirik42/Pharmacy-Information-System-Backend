from pydantic import Field

from .base import Base


class DrugType(Base):
    name: str = Field(max_length=256)
    cookable: bool
