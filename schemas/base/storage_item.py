from datetime import datetime

from pydantic import Field

from .base import BaseSchema
from .drug import DrugSchema


class StorageItemSchema(BaseSchema):
    id: int = Field(ge=1)
    drug: DrugSchema
    available_amount: int = Field(ge=0)
    original_amount: int = Field(ge=1)
    receipt_datetime: datetime
