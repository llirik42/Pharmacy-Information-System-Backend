from sqladmin import ModelView

from models import Tincture


class TinctureView(ModelView, model=Tincture):
    column_list = [
        Tincture.drug_id,
        Tincture.material
    ]
