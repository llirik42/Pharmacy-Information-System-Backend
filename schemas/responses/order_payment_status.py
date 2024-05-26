from enum import StrEnum, auto


class OrderPaymentStatus(StrEnum):
    SUCCESS = (auto(),)
    NOT_FOUND = (auto(),)
    CANNOT_BE_PAID = (auto(),)
    ALREADY_PAID = (auto(),)
