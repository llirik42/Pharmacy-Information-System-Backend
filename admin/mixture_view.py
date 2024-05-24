from models import Mixture

from .base import BaseView


class MixtureView(BaseView, model=Mixture):
    column_list = [Mixture.drug, Mixture.solvent, Mixture.mixture_type]
