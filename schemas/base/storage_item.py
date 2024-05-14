from datetime import datetime

from pydantic import BaseModel, Field

from .drug import Drug


class StorageItem(BaseModel):
    drug: Drug
    available_amount: int = Field(ge=0)
    original_amount: int = Field(ge=1)
    receipt_datetime: datetime
