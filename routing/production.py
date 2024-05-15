from fastapi import APIRouter

from schemas import TechnologyComponent

router = APIRouter(prefix="/production")


@router.get("/components")
async def get_production_components() -> list[TechnologyComponent]:
    return []
