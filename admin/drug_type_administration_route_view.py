from sqladmin import ModelView

from models import DrugTypeAdministrationRoute


class DrugTypeAdministrationRouteView(ModelView, model=DrugTypeAdministrationRoute):
    column_list = [
        DrugTypeAdministrationRoute.type_id,
        DrugTypeAdministrationRoute.route_id,
    ]
