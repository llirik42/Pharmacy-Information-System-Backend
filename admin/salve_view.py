from sqladmin import ModelView

from models import Salve


class SalveView(ModelView, model=Salve):
    column_list = [
        Salve.drug_id,
        Salve.active_substance
    ]
