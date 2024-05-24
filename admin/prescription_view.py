from models import Prescription

from .base import BaseView


class PrescriptionView(BaseView, model=Prescription):
    column_list = [
        Prescription.id,
        Prescription.patient,
        Prescription.doctor,
        Prescription.date,
    ]

    column_details_exclude_list = [Prescription.items]

    form_excluded_columns = [Prescription.items]
