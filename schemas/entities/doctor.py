from pydantic import Field

from ..input import InputDoctorSchema


class DoctorSchema(InputDoctorSchema):
    id: int = Field(ge=1)
