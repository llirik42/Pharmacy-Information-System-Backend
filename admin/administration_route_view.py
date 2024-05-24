from sqladmin import ModelView

from models import AdministrationRoute


class AdministrationRouteView(ModelView, model=AdministrationRoute):
    column_list = [
        AdministrationRoute.id,
        AdministrationRoute.description
    ]
