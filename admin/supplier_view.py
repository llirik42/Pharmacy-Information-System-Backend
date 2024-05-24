from sqladmin import ModelView

from models import Supplier


class SupplierView(ModelView, model=Supplier):
    column_list = [
        Supplier.id,
        Supplier.name,
        Supplier.phone_number
    ]
