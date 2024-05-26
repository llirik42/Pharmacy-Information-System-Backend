from pydantic import Field

from .base import BaseSchema


class DoctorSchema(BaseSchema):
    id: int = Field(ge=1)
    full_name: str = Field(max_length=256)
