from pydantic import Field

from .base import Base
from .drug import Drug


class TechnologyComponent(Base):
    component: Drug
    component_amount: int = Field(ge=1)
