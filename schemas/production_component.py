from pydantic import Field

from .base.base import Base
from .base.drug import Drug


class ProductionComponent(Base):
    component: Drug
    component_amount: int = Field(ge=1)
