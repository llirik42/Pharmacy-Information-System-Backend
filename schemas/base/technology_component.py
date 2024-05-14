from pydantic import BaseModel, Field

from .drug import Drug


class TechnologyComponent(BaseModel):
    component: Drug
    component_amount: Drug = Field(ge=1)
