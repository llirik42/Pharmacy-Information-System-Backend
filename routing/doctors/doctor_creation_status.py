from enum import StrEnum, auto


class DoctorCreationStatus(StrEnum):
    SUCCESS = auto()
    ALREADY_EXISTS = auto()
