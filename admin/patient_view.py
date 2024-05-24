from sqladmin import ModelView

from models import Patient


class PatientView(ModelView, model=Patient):
    column_list = [
        Patient.id,
        Patient.full_name,
        Patient.birthday
    ]
