from enum import StrEnum, auto


class OrderObtainStatus(StrEnum):
    SUCCESS = (auto(),)
    NOT_FOUND = (auto(),)
    CANNOT_BE_OBTAINED = (auto(),)
    ALREADY_OBTAINED = (auto(),)
