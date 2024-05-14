from datetime import date

from pydantic import BaseModel, Field


class Patient(BaseModel):
    full_name: str = Field(max_length=256)
    birth_date: date = Field(validation_alias='birthday')
