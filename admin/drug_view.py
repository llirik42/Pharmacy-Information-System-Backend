from sqladmin import ModelView

from models import Drug


class DrugView(ModelView, model=Drug):
    column_list = [
        Drug.id,
        Drug.name,
        Drug.cost,
        Drug.shelf_life,
        Drug.critical_amount,
        Drug.type_id,
        Drug.description
    ]
