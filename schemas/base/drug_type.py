from pydantic import BaseModel, Field


class DrugType(BaseModel):
    name: str = Field(max_length=256)
    cookable: bool
