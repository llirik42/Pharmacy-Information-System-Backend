from pydantic import Field

from .base.base import Base
from .base.drug import Drug


class UsedDrug(Base):
    drug: Drug
    use_number: int = Field(ge=0)
