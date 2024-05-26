from pydantic import Field

from schemas import BaseSchema
from .customer_creation_status import CustomerCreationStatus


class CustomerCreationResponseSchema(BaseSchema):
    status: CustomerCreationStatus
    customer_id: int = Field(ge=1, default=0)
