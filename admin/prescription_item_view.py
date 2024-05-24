from models import PrescriptionItem

from .base import BaseView


class PrescriptionItemView(BaseView, model=PrescriptionItem):
    column_list = [
        PrescriptionItem.prescription_id,
        PrescriptionItem.drug,
        PrescriptionItem.amount,
        PrescriptionItem.administration_route,
    ]

    name_plural = "Prescriptions items"
