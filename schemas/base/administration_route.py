from pydantic import Field

from .base import BaseSchema


class AdministrationRouteSchema(BaseSchema):
    id: int = Field(ge=1)
    description: str = Field(max_length=256)
