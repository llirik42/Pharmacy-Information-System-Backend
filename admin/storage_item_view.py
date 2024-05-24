from sqladmin import ModelView

from models import StorageItem


class StorageItemView(ModelView, model=StorageItem):
    column_list = [
        StorageItem.id,
        StorageItem.drug_id,
        StorageItem.available_amount,
        StorageItem.original_amount,
        StorageItem.receipt_datetime
    ]
