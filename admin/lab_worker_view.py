from sqladmin import ModelView

from models import LabWorker


class LabWorkerView(ModelView, model=LabWorker):
    column_list = [
        LabWorker.id,
        LabWorker.full_name,
    ]
