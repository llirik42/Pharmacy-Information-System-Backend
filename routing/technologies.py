from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session
from models import TechnologyOrm
from schemas import Technology

router = APIRouter(prefix="/technologies")


@router.get("/")
async def get_technologies(
    drug_id: Optional[int] = None,
    drug_type_id: Optional[int] = None,
    in_production: bool = False,
    session: AsyncSession = Depends(get_session),
) -> list[Technology]:
    query = text(
        _get_technologies_query_string(drug_id=drug_id, drug_type_id=drug_type_id, in_production=in_production)
    )
    query_result = await session.execute(query)

    technologies: list[Technology] = []

    for row in query_result:
        technology_id: int = row[0]
        technology_orm = await session.get(TechnologyOrm, ident=technology_id)
        technologies.append(Technology.model_validate(technology_orm))

    return technologies


def _get_technologies_query_string(
    drug_id: Optional[int] = None, drug_type_id: Optional[int] = None, in_production: bool = False
) -> str:
    if drug_id is not None and in_production:
        return f"""
            select distinct
                technologies.id as technology_id
            from technologies
                join production on technologies.id = production.technology_id
            where technologies.drug_id = {drug_id}
        """

    if drug_id is not None and not in_production:
        return f"""
            select
                id as technology_id
            from technologies
            where drug_id = {drug_id}
        """

    if drug_type_id is not None and in_production:
        return f"""
            select distinct
                technologies.id as technology_id
            from technologies
                join production on technologies.id = production.technology_id
                join drugs on technologies.drug_id = drugs.id
            where drugs.type_id = {drug_type_id}
        """

    if drug_type_id is not None and not in_production:
        return f"""
            select
                technologies.id as technology_id
            from technologies
                join drugs on technologies.drug_id = drugs.id
            where drugs.type_id = {drug_type_id}
        """

    if in_production:
        return """
            select distinct
                technologies.id as technology_id
            from technologies
                join production on technologies.id = production.technology_id
        """

    return """
        select id as technology_id
        from technologies
    """
