from models import AdministrationRoute

from .base import BaseView


class AdministrationRouteView(BaseView, model=AdministrationRoute):
    column_list = [AdministrationRoute.id, AdministrationRoute.description]
