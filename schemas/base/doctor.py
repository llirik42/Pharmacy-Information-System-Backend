from pydantic import BaseModel, Field


class Doctor(BaseModel):
    full_name: str = Field(max_length=256)
