from datetime import date

from pydantic import Field

from .base import Base


class Patient(Base):
    id: int = Field(ge=1)
    full_name: str = Field(max_length=256)
    birthday: date
