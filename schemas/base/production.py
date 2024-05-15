from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .order import Order
from .technology import Technology
from .base import Base


class Production(Base):
    order: Order
    technology: Technology
    drug_amount: int = Field(ge=1)
    start: Optional[datetime] = None
    end: Optional[datetime] = None
