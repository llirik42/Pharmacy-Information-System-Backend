from datetime import datetime

from pydantic import BaseModel, Field

from .drug import Drug
from .base import Base


class StorageItem(Base):
    drug: Drug
    available_amount: int = Field(ge=0)
    original_amount: int = Field(ge=1)
    receipt_datetime: datetime
