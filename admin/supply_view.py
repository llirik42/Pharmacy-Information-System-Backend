from models import Supply

from .base import BaseView


class SupplyView(BaseView, model=Supply):
    column_list = [
        Supply.id,
        Supply.drug,
        Supply.supplier,
        Supply.drug_amount,
        Supply.cost,
        Supply.assigned_datetime,
        Supply.delivery_datetime,
    ]

    name_plural = "Supplies"
