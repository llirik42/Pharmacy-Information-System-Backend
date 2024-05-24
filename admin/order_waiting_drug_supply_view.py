from models import OrderWaitingDrugSupply

from .base import BaseView


class OrderWaitingDrugSupplyView(BaseView, model=OrderWaitingDrugSupply):
    column_list = [OrderWaitingDrugSupply.order_id, OrderWaitingDrugSupply.drug, OrderWaitingDrugSupply.amount]

    name_plural = "Orders Waiting Drug Supplies"
