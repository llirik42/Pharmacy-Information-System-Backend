from ..base.base import Base


class BaseResponse(Base):
    message: str = "success"
    success: bool = True
