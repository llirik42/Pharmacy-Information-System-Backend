from pydantic import Field

from .base import BaseSchema


class DrugTypeSchema(BaseSchema):
    id: int = Field(ge=1)
    name: str = Field(max_length=256)
    cookable: bool
