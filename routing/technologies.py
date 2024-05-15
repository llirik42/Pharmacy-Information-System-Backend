from typing import Optional

from fastapi import APIRouter

from schemas import Technology

router = APIRouter(prefix="/technologies")


@router.get("/technologies")
async def get_technologies(
    drug_id: Optional[int] = None,
    drug_type_id: Optional[int] = None,
    in_production: bool = False,
    session: AsyncSession = Depends(get_session),
) -> list[Technology]:
    return []
