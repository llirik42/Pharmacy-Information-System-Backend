from pydantic import Field

from .base import Base


class AdministrationRoute(Base):
    id: int = Field(ge=1)
    description: str = Field(max_length=256)
