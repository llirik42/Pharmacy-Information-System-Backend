from .abstract_prescription import AbstractPrescription
from .short_prescription_item import ShortPrescriptionItem


class ShortPrescription(AbstractPrescription):
    items: [ShortPrescriptionItem]
