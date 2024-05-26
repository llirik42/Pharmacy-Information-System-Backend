from pydantic import Field

from ..input import InputPatientSchema


class PatientSchema(InputPatientSchema):
    id: int = Field(ge=1)
