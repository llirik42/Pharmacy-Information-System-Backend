from pydantic import Field

from .base.base import BaseSchema
from .base.drug import DrugSchema


class ProductionComponentSchema(BaseSchema):
    component: DrugSchema
    component_amount: int = Field(ge=1)
