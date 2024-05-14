from pydantic import BaseModel, Field

from .drug import Drug
from .administration_route import AdministrationRoute


class PrescriptionItem(BaseModel):
    drug: Drug
    amount: int = Field(ge=1)
    administration_route: AdministrationRoute
