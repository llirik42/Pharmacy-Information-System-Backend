from datetime import date

from pydantic import Field

from ..base import BaseSchema


class InputPatientSchema(BaseSchema):
    full_name: str = Field(max_length=256)
    birthday: date
