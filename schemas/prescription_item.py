from pydantic import Field

from .base import BaseSchema
from .entities import AdministrationRouteSchema, DrugSchema


class PrescriptionItemSchema(BaseSchema):
    drug: DrugSchema
    amount: int = Field(ge=1)
    administration_route: AdministrationRouteSchema
