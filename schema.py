from pydantic import BaseModel


class AdministrationRoute(BaseModel):
    description: str
