from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import BaseSchema
from .drug import DrugSchema
from .supplier import SupplierSchema


class SupplySchema(BaseSchema):
    id: int = Field(ge=1)
    drug: DrugSchema
    drug_amount: int = Field(ge=1)
    cost: int = Field(ge=0)
    assigned_datetime: datetime
    delivery_datetime: Optional[datetime] = None
    supplier: SupplierSchema
