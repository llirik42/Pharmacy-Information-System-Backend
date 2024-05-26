from pydantic import Field

from .base import BaseSchema
from .entities.drug import DrugSchema


class UsedDrugSchema(BaseSchema):
    drug: DrugSchema
    use_number: int = Field(ge=0)
