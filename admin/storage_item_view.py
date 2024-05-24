from models import StorageItem

from .base import BaseView


class StorageItemView(BaseView, model=StorageItem):
    column_list = [
        StorageItem.id,
        StorageItem.drug,
        StorageItem.available_amount,
        StorageItem.original_amount,
        StorageItem.receipt_datetime,
    ]
