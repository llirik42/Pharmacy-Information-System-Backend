from sqladmin import ModelView

from models import Solution


class SolutionView(ModelView, model=Solution):
    column_list = [
        Solution.drug_id,
        Solution.dosage
    ]
