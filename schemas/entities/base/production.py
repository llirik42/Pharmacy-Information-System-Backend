from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import BaseSchema
from .order import OrderSchema
from .technology import TechnologySchema


class ProductionSchema(BaseSchema):
    id: int = Field(ge=1)
    order: OrderSchema
    technology: TechnologySchema
    drug_amount: int = Field(ge=1)
    start: Optional[datetime] = None
    end: Optional[datetime] = None
