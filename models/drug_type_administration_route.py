from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .administration_route import AdministrationRoute
from .base import Base
from .drug_type import DrugType


class DrugTypeAdministrationRoute(Base):
    __tablename__ = "drug_types_administration_routes"

    type_id: Mapped[int] = mapped_column(ForeignKey("drug_types.id"), primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey("administration_routes.id"), primary_key=True)
    type: Mapped[DrugType] = relationship()
    route: Mapped[AdministrationRoute] = relationship()
