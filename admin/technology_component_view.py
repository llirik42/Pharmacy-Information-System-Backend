from sqladmin import ModelView

from models import TechnologyComponent


class TechnologyComponentView(ModelView, model=TechnologyComponent):
    column_list = [
        TechnologyComponent.technology_id,
        TechnologyComponent.component_id,
        TechnologyComponent.component_amount
    ]
