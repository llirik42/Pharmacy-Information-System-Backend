from sqladmin import ModelView

from models import Production


class ProductionView(ModelView, model=Production):
    column_list = [
        Production.id,
        Production.order_id,
        Production.technology_id,
        Production.drug_amount,
        Production.start,
        Production.end
    ]
