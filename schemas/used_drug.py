from pydantic import Field

from schemas.base.drug import Drug


class UsedDrug(Drug):
    uses_number: int = Field(ge=0)
