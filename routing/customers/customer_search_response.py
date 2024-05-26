from typing import Optional

from schemas import BaseSchema, CustomerSchema


class CustomerSearchResponseSchema(BaseSchema):
    customer: Optional[CustomerSchema] = None
