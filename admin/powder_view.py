from sqladmin import ModelView

from models import Powder


class PowderView(ModelView, model=Powder):
    column_list = [
        Powder.drug_id,
        Powder.composite
    ]
