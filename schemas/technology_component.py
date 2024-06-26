from pydantic import Field

from .base import BaseSchema
from .entities.drug import DrugSchema


class TechnologyComponentSchema(BaseSchema):
    component: DrugSchema
    component_amount: int = Field(ge=1)
