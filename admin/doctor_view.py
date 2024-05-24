from models import Doctor

from .base import BaseView


class DoctorView(BaseView, model=Doctor):
    column_list = [
        Doctor.id,
        Doctor.full_name,
    ]
