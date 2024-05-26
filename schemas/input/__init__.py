__all__ = [
    "InputPatientSchema",
    "InputDoctorSchema",
    "InputCustomerSchema",
    "InputPrescriptionSchema",
    "InputPrescriptionItemSchema",
    "InputOrderSchema",
]

from .input_customer import InputCustomerSchema
from .input_doctor import InputDoctorSchema
from .input_order import InputOrderSchema
from .input_patient import InputPatientSchema
from .input_prescription import InputPrescriptionSchema
from .input_prescription_item import InputPrescriptionItemSchema
