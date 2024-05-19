from enum import IntEnum


class DoctorResponseStatus(IntEnum):
    SUCCESS = (0,)
    INVALID = (1,)
    NOT_FOUND = (2,)
