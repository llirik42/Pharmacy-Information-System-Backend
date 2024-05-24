from models import ProductionLabWorker

from .base import BaseView


class ProductionLabWorkerView(BaseView, model=ProductionLabWorker):
    column_list = [
        ProductionLabWorker.production_id,
        ProductionLabWorker.lab_worker,
    ]
