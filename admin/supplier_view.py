from models import Supplier

from .base import BaseView


class SupplierView(BaseView, model=Supplier):
    column_list = [Supplier.id, Supplier.name, Supplier.phone_number]
