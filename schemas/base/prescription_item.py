from pydantic import BaseModel, Field

from .administration_route import AdministrationRoute
from .drug import Drug
from .base import Base


class PrescriptionItem(Base):
    drug: Drug
    amount: int = Field(ge=1)
    administration_route: AdministrationRoute
