from sqladmin import ModelView

from models import DrugType


class DrugTypeView(ModelView, model=DrugType):
    column_list = [
        DrugType.id,
        DrugType.name,
        DrugType.cookable
    ]
