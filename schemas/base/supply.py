from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .drug import Drug
from .supplier import Supplier


class Supply(BaseModel):
    drug: Drug
    drug_amount: int = Field(ge=1)
    cost: int = Field(ge=0)
    assigned_datetime: datetime
    delivery_datetime: Optional[datetime] = None
    supplier: Supplier
