from sqladmin import ModelView

from models import ReservedDrug


class ReservedDrugView(ModelView, model=ReservedDrug):
    column_list = [
        ReservedDrug.order_id,
        ReservedDrug.storage_item_id,
        ReservedDrug.drug_amount
    ]
