from sqladmin import ModelView

from models import Doctor


class DoctorView(ModelView, model=Doctor):
    column_list = [
        Doctor.id,
        Doctor.full_name,
    ]
