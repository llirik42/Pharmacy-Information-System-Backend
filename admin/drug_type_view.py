from models import DrugType

from .base import BaseView


class DrugTypeView(BaseView, model=DrugType):
    column_list = [DrugType.id, DrugType.name, DrugType.cookable]
