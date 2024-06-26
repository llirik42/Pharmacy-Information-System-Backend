from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class AdministrationRoute(Base):
    __tablename__ = "administration_routes"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(256), unique=True)

    def __repr__(self) -> str:
        return self.description
