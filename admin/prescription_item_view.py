from sqladmin import ModelView

from models import PrescriptionItem


class PrescriptionItemView(ModelView, model=PrescriptionItem):
    column_list = [
        PrescriptionItem.prescription_id,
        PrescriptionItem.drug_id,
        PrescriptionItem.amount,
        PrescriptionItem.administration_route_id
    ]
