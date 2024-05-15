from pydantic import Field

from .base import Base
from .drug_type import DrugType


class Drug(Base):
    name: str = Field(max_length=256)
    cost: int = Field(ge=1)
    shelf_life: int = Field(ge=1)
    critical_amount: int = Field(ge=0)
    drug_type: DrugType
    description: str = Field(max_length=256)
