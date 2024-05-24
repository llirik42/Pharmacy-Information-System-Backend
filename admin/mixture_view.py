from sqladmin import ModelView

from models import Mixture


class MixtureView(ModelView, model=Mixture):
    column_list = [
        Mixture.drug_id,
        Mixture.solvent,
        Mixture.mixture_type_id
    ]
