from datetime import datetime

from pydantic import Field

from .base import Base
from .drug import Drug


class StorageItem(Base):
    drug: Drug
    available_amount: int = Field(ge=0)
    original_amount: int = Field(ge=1)
    receipt_datetime: datetime
