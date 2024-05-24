from models import Order

from .base import BaseView


class OrderView(BaseView, model=Order):
    column_list = [
        Order.id,
        Order.prescription_id,
        Order.registration_datetime,
        Order.appointed_datetime,
        Order.obtaining_datetime,
        Order.paid,
        Order.customer,
    ]

    column_details_exclude_list = [Order.prescription]

    form_excluded_columns = [Order.prescription]
