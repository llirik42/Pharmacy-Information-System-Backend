from .abstract_prescription_item import AbstractPrescriptionItem
from .short_drug import ShortDrug


class ShortPrescriptionItem(AbstractPrescriptionItem):
    drug: ShortDrug
