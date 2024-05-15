from pydantic import Field

from .base import Base


class LabWorker(Base):
    full_name: str = Field(max_length=256)
