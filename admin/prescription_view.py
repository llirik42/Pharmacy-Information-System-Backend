from sqladmin import ModelView

from models import Prescription


class PrescriptionView(ModelView, model=Prescription):
    column_list = [
        Prescription.id,
        Prescription.diagnosis,
        Prescription.patient_id,
        Prescription.doctor_id,
        Prescription.date,
    ]
