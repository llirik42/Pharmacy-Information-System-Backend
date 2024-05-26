from pydantic import Field

from .administration_route import AdministrationRouteSchema
from .base import BaseSchema
from .drug import DrugSchema


class PrescriptionItemSchema(BaseSchema):
    drug: DrugSchema
    amount: int = Field(ge=1)
    administration_route: AdministrationRouteSchema
