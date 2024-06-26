from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import Drug
from schemas import ProductionComponentSchema, DrugSchema

router = APIRouter(prefix="/production")


@router.get("/components")
async def get_production_components(session: AsyncSession = Depends(get_session)) -> list[ProductionComponentSchema]:
    query = text(_get_production_components_query_string())
    query_result = await session.execute(query)

    production_components: list[ProductionComponentSchema] = []

    for row in query_result:
        drug_id: int = row[0]
        drug = await session.get(Drug, ident=drug_id)

        production_components.append(
            ProductionComponentSchema(
                component=DrugSchema.model_validate(drug),
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
        order by component_amount desc
    """
