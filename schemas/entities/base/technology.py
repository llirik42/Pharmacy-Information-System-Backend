from datetime import time

from pydantic import Field

from .base import BaseSchema
from .drug import DrugSchema
from .technology_component import TechnologyComponentSchema


class TechnologySchema(BaseSchema):
    id: int = Field(ge=1)
    drug: DrugSchema
    cooking_time: time
    amount: int = Field(ge=1)
    description: str = Field(max_length=256)
    components: list[TechnologyComponentSchema]
