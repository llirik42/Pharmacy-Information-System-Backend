from pydantic import Field

from .base.base import Base
from .base.drug import Drug


class StoredDrug(Base):
    drug: Drug
    stored_number: int = Field(ge=0)
