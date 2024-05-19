from pydantic import Field

from .base import Base


class LabWorker(Base):
    id: int = Field(ge=1)
    full_name: str = Field(max_length=256)
