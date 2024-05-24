from models import Powder

from .base import BaseView


class PowderView(BaseView, model=Powder):
    column_list = [Powder.drug, Powder.composite]
