from pydantic import BaseModel, Field

from .base.drug import Drug


class ProductionComponent(BaseModel):
    component: Drug
    component_amount: int = Field(ge=1)
