from models import Production

from .base import BaseView


class ProductionView(BaseView, model=Production):
    column_list = [
        Production.id,
        Production.order_id,
        Production.technology_id,
        Production.drug_amount,
        Production.start,
        Production.end,
    ]

    name_plural = "Production"
