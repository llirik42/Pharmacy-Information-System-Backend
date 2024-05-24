from sqladmin import ModelView

from models import Order


class OrderView(ModelView, model=Order):
    column_list = [
        Order.id,
        Order.prescription_id,
        Order.registration_datetime,
        Order.appointed_datetime,
        Order.obtaining_datetime,
        Order.paid,
        Order.customer_id,
    ]
