from models import Drug

from .base import BaseView


class DrugView(BaseView, model=Drug):
    column_list = [
        Drug.id,
        Drug.name,
        Drug.description,
        Drug.drug_type,
        Drug.cost,
        Drug.shelf_life,
        Drug.critical_amount,
    ]
