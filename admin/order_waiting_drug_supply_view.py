from sqladmin import ModelView

from models import OrderWaitingDrugSupply


class OrderWaitingDrugSupplyView(ModelView, model=OrderWaitingDrugSupply):
    column_list = [
        OrderWaitingDrugSupply.order_id,
        OrderWaitingDrugSupply.drug_id,
        OrderWaitingDrugSupply.amount
    ]
