from sqladmin import ModelView

from models import MixtureType


class MixtureTypeView(ModelView, model=MixtureType):
    column_list = [
        MixtureType.id,
        MixtureType.name,
    ]
