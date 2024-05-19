from pydantic import Field

from .base import Base


class Doctor(Base):
    id: int = Field(ge=1)
    full_name: str = Field(max_length=256)
