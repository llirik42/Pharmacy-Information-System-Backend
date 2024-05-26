from schemas import BaseSchema

from .customer_creation_status import CustomerCreationStatus


class CustomerCreationResponseSchema(BaseSchema):
    status: CustomerCreationStatus
