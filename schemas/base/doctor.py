from pydantic import Field

from .base import Base


class Doctor(Base):
    full_name: str = Field(max_length=256)
