from typing import Optional

from pydantic import Field

from ..base import BaseSchema


class InputOrderSchema(BaseSchema):
    prescription_id: int = Field(ge=1)
    customer_id: Optional[int] = Field(default=None, ge=1)
