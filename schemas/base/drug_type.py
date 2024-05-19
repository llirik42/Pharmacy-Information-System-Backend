from pydantic import Field

from .base import Base


class DrugType(Base):
    id: int
    name: str = Field(max_length=256)
    cookable: bool
