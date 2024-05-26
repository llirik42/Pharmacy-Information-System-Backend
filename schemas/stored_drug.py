from pydantic import Field

from .base.base import BaseSchema
from .base.drug import DrugSchema


class StoredDrugSchema(BaseSchema):
    drug: DrugSchema
    stored_number: int = Field(ge=0)
