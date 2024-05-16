from datetime import date

from pydantic import Field

from .base import Base


class Patient(Base):
    full_name: str = Field(max_length=256)
    birthday: date
