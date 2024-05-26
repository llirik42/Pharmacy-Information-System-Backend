from pydantic import Field

from .drug_type import DrugTypeSchema
from ..base import BaseSchema


class DrugSchema(BaseSchema):
    id: int = Field(ge=1)
    name: str = Field(max_length=256)
    cost: int = Field(ge=1)
    shelf_life: int = Field(ge=1)
    critical_amount: int = Field(ge=0)
    drug_type: DrugTypeSchema
    description: str = Field(max_length=256)
