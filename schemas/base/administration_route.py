from pydantic import Field

from .base import Base


class AdministrationRoute(Base):
    description: str = Field(max_length=256)
