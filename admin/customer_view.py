from sqladmin import ModelView

from models import Customer


class CustomerView(ModelView, model=Customer):
    column_list = [
        Customer.id,
        Customer.full_name,
        Customer.phone_number,
        Customer.address
    ]
