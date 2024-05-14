from pydantic import BaseModel, Field


class AdministrationRoute(BaseModel):
    description: str = Field(max_length=256)
