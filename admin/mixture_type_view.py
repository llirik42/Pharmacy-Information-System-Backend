from models import MixtureType

from .base import BaseView


class MixtureTypeView(BaseView, model=MixtureType):
    column_list = [
        MixtureType.id,
        MixtureType.name,
    ]
