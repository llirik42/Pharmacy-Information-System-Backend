from sqladmin import ModelView

from models import Pill


class PillView(ModelView, model=Pill):
    column_list = [
        Pill.drug_id,
        Pill.weight_of_pill,
        Pill.pills_count
    ]
