from models import Technology

from .base import BaseView


class TechnologyView(BaseView, model=Technology):
    column_list = [
        Technology.id,
        Technology.drug,
        Technology.cooking_time,
        Technology.amount,
    ]

    column_details_exclude_list = [Technology.components]

    form_excluded_columns = [Technology.components]

    name_plural = "Technologies"
