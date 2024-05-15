from pydantic import Field

from .drug_type import DrugType
from .short_drug import ShortDrug


class Drug(ShortDrug):
    cost: int = Field(ge=1)
    shelf_life: int = Field(ge=1)
    critical_amount: int = Field(ge=0)
    drug_type: DrugType
    description: str = Field(max_length=256)
