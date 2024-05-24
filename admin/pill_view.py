from models import Pill

from .base import BaseView


class PillView(BaseView, model=Pill):
    column_list = [Pill.drug, Pill.weight_of_pill, Pill.pills_count]
