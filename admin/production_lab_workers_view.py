from sqladmin import ModelView

from models import ProductionLabWorker


class ProductionLabWorkerView(ModelView, model=ProductionLabWorker):
    column_list = [
        ProductionLabWorker.production_id,
        ProductionLabWorker.lab_worker_id,
    ]
