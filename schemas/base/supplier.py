from pydantic import BaseModel, Field


class Supplier(BaseModel):
    name: str = Field(max_length=256)
    phone_number: str = Field(max_length=32)
