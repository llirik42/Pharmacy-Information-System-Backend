from pydantic import BaseModel, Field

from .drug import Drug
from .base import Base


class TechnologyComponent(Base):
    component: Drug
    component_amount: Drug = Field(ge=1)
