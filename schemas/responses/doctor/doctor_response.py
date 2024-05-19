from typing import Optional

from schemas import Doctor
from schemas import Base
from .doctor_response_status import DoctorResponseStatus


class DoctorResponse(Base):
    status: DoctorResponseStatus = DoctorResponseStatus.SUCCESS
    doctor: Optional[Doctor] = None
