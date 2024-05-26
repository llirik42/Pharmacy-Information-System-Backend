from enum import StrEnum, auto


class CustomerCreationStatus(StrEnum):
    SUCCESS = auto()
    ALREADY_EXISTS_OR_INVALID = auto()
