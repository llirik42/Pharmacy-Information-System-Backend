from models import DrugTypeAdministrationRoute

from .base import BaseView


class DrugTypeAdministrationRouteView(BaseView, model=DrugTypeAdministrationRoute):
    column_list = [
        DrugTypeAdministrationRoute.type,
        DrugTypeAdministrationRoute.route,
    ]

    name_plural = "Drug Types Administration Routes"
