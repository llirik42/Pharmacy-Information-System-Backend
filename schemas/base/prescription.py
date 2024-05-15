from .abstract_prescription import AbstractPrescription
from .prescription_item import PrescriptionItem


class Prescription(AbstractPrescription):
    items: list[PrescriptionItem]
