from pydantic import BaseModel, Field


class Doctor(BaseModel):
    full_name: str = Field(max_length=256)

    class Config:
        from_attributes = True
