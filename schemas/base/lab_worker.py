from pydantic import BaseModel, Field


class LabWorker(BaseModel):
    full_name: str = Field(max_length=256)
