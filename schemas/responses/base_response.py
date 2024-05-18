from ..base.base import Base


class BaseResponse(Base):
    message: str = "success"
    is_success: bool = True


def create_error_base_response(message: str) -> BaseResponse:
    return BaseResponse(is_success=False, message=message)
