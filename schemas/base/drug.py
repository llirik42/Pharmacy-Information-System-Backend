from pydantic import BaseModel, Field

from schemas.base.drug_type import DrugType


class Drug(BaseModel):
    name: str = Field(max_length=256)
    cost: int = Field(ge=1)
    shelf_life: int = Field(ge=1)
    critical_amount: int = Field(ge=0)
    type: DrugType
    description: str = Field(max_length=256)
