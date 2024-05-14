from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .order import Order
from .technology import Technology


class Production(BaseModel):
    order: Order
    technology: Technology
    drug_amount: int = Field(ge=1)
    start: Optional[datetime] = None
    end: Optional[datetime] = None
