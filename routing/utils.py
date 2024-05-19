from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession

from models import Base


def date_to_mysql_string(d: date) -> str:
    return f"'{str(d).replace('-', '/')}'"


async def create_object(session: AsyncSession, obj: Base) -> None:
    session.add(obj)
    await session.flush()
    await session.refresh(obj)
