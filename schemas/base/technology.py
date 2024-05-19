from datetime import time

from pydantic import Field

from .base import Base
from .drug import Drug
from .technology_component import TechnologyComponent


class Technology(Base):
    id: int = Field(ge=1)
    drug: Drug
    cooking_time: time
    amount: int = Field(ge=1)
    description: str = Field(max_length=256)
    components: list[TechnologyComponent]
