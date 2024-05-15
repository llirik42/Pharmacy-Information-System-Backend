from pydantic import Field

from .administration_route import AdministrationRoute
from .base import Base


class AbstractPrescriptionItem(Base):
    amount: int = Field(ge=1)
    administration_route: AdministrationRoute
