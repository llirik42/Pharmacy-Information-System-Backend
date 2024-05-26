from enum import StrEnum, auto


class PatientCreationStatus(StrEnum):
    SUCCESS = auto()
    ALREADY_EXISTS = auto()
