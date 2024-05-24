from sqladmin import ModelView

from models import Technology


class TechnologyView(ModelView, model=Technology):
    column_list = [
        Technology.id,
        Technology.drug_id,
        Technology.cooking_time,
        Technology.amount,
        Technology.description,
    ]
