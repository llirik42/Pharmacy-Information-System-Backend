from ..base.base import Base


class BaseResponse(Base):
    message: str = "success"
    is_success: bool = True
