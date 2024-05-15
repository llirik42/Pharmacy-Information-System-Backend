from .abstract_prescription_item import AbstractPrescriptionItem
from .drug import Drug


class PrescriptionItem(AbstractPrescriptionItem):
    drug: Drug
