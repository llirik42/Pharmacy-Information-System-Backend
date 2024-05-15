from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import DrugOrm
from schemas import TechnologyComponent, Drug

router = APIRouter(prefix="/production")


@router.get("/components")
async def get_production_components(session: AsyncSession = Depends(get_session)) -> list[TechnologyComponent]:
    query = text(
        """
        select
            technology_components.component_id,
            sum(production.drug_amount * technology_components.component_amount) as component_amount
        from production
            join technologies on production.technology_id = technologies.id
            join technology_components on technologies.id = technology_components.technology_id
        group by technology_components.component_id
        """
    )

    result = await session.execute(query)

    components: list[TechnologyComponent] = []

    for i in result:
        drug_res = await session.get(DrugOrm, ident=i[0])
        components.append(
            TechnologyComponent(
                component=Drug.model_validate(drug_res),
                component_amount=i[1],
            )
        )

    return components
