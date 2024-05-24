from models import LabWorker

from .base import BaseView


class LabWorkerView(BaseView, model=LabWorker):
    column_list = [
        LabWorker.id,
        LabWorker.full_name,
    ]
