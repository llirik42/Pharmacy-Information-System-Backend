from pydantic import Field

from .base.base import BaseSchema
from .base.drug import DrugSchema


class UsedDrugSchema(BaseSchema):
    drug: DrugSchema
    use_number: int = Field(ge=0)
