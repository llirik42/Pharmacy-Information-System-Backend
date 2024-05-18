from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugOrm
from schemas import ProductionComponent, Drug

router = APIRouter(prefix="/production")


@router.get("/components")
async def get_production_components(session: AsyncSession = Depends(get_session)) -> list[ProductionComponent]:
    query = text(_get_production_components_query_string())
    query_result = await session.execute(query)

    production_components: list[ProductionComponent] = []

    for row in query_result:
        drug_id: int = row[0]
        drug_orm = await session.get(DrugOrm, ident=drug_id)

        production_components.append(
            ProductionComponent(
                component=Drug.model_validate(drug_orm),
                component_amount=row[1],
            )
        )

    return production_components


def _get_production_components_query_string() -> str:
    return """
        select
            technology_components.component_id,
            sum(production.drug_amount * technology_components.component_amount) as component_amount
        from production
            join technologies on production.technology_id = technologies.id
            join technology_components on technologies.id = technology_components.technology_id
        group by technology_components.component_id
    """
