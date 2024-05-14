from pydantic import Field

from .base.drug import Drug


class StoredDrug(Drug):
    stored_count: int = Field(ge=0)
