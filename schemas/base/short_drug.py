from pydantic import Field

from .base import Base


class ShortDrug(Base):
    name: str = Field(max_length=256)
