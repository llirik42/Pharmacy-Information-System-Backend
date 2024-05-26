from pydantic import Field

from .base import BaseSchema
from .entities.drug import DrugSchema


class StoredDrugSchema(BaseSchema):
    drug: DrugSchema
    stored_number: int = Field(ge=0)
