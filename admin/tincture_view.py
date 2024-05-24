from models import Tincture

from .base import BaseView


class TinctureView(BaseView, model=Tincture):
    column_list = [Tincture.drug, Tincture.material]
