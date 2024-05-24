from models import Customer

from .base import BaseView


class CustomerView(BaseView, model=Customer):
    column_list = [Customer.id, Customer.full_name, Customer.phone_number, Customer.address]
