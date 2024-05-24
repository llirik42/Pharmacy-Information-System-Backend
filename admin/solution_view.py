from models import Solution

from .base import BaseView


class SolutionView(BaseView, model=Solution):
    column_list = [Solution.drug, Solution.dosage]
