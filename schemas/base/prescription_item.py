from pydantic import BaseModel, Field

from .administration_route import AdministrationRoute
from .drug import Drug


class PrescriptionItem(BaseModel):
    drug: Drug
    amount: int = Field(ge=1)
    administration_route: AdministrationRoute
