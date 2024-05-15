from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import Base
from .order import Order
from .technology import Technology


class Production(Base):
    order: Order
    technology: Technology
    drug_amount: int = Field(ge=1)
    start: Optional[datetime] = None
    end: Optional[datetime] = None
