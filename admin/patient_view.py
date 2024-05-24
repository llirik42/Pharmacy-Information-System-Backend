from models import Patient

from .base import BaseView


class PatientView(BaseView, model=Patient):
    column_list = [Patient.id, Patient.full_name, Patient.birthday]
