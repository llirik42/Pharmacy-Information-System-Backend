from typing import Optional

from schemas import BaseSchema, OrderSchema


class OrderSearchResponseSchema(BaseSchema):
    order: Optional[OrderSchema] = None
