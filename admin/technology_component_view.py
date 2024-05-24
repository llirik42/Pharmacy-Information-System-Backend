from models import TechnologyComponent

from .base import BaseView


class TechnologyComponentView(BaseView, model=TechnologyComponent):
    column_list = [
        TechnologyComponent.technology_id,
        TechnologyComponent.component,
        TechnologyComponent.component_amount,
    ]
