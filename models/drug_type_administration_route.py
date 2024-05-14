from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DrugTypeAdministrationRouteOrm(Base):
    __tablename__ = 'drug_types_administration_routes'

    type_id: Mapped[int] = mapped_column(ForeignKey('drug_types.id'), primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey('administration_routes.id'), primary_key=True)
