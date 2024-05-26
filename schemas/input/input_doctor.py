from pydantic import Field

from ..base import BaseSchema


class InputDoctorSchema(BaseSchema):
    full_name: str = Field(max_length=256)
