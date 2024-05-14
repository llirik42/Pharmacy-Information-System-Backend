from pydantic import BaseModel, Field


class Customer(BaseModel):
    full_name: str = Field(max_length=256)
    phone_number: str = Field(max_length=32)
    address: str = Field(max_length=256)
