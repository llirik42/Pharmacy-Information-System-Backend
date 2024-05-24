from models import ReservedDrug

from .base import BaseView


class ReservedDrugView(BaseView, model=ReservedDrug):
    column_list = [ReservedDrug.order_id, ReservedDrug.storage_item_id, ReservedDrug.drug_amount]
