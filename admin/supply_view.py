from sqladmin import ModelView

from models import Supply


class SupplyView(ModelView, model=Supply):
    column_list = [
        Supply.id,
        Supply.drug_id,
        Supply.drug_amount,
        Supply.cost,
        Supply.assigned_datetime,
        Supply.delivery_datetime,
        Supply.supplier_id
    ]
