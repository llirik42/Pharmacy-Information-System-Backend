from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import AdministrationRoute
from schemas import AdministrationRouteSchema

router = APIRouter(prefix="/administration-routes")


@router.get("/")
async def get_administration_routes(session: AsyncSession = Depends(get_session)) -> list[AdministrationRouteSchema]:
    query = select(AdministrationRoute)
    query_result = await session.execute(query)
    return [AdministrationRouteSchema.model_validate(a) for a in query_result.scalars().all()]
