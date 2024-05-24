from models import Salve

from .base import BaseView


class SalveView(BaseView, model=Salve):
    column_list = [Salve.drug, Salve.active_substance]
