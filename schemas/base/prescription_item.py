from pydantic import Field

from .administration_route import AdministrationRoute
from .base import Base
from .drug import Drug


class PrescriptionItem(Base):
    drug: Drug
    amount: int = Field(ge=1)
    administration_route: AdministrationRoute
