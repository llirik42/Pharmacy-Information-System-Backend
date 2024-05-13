from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from settings import settings

DATABASE_URL = (f"mysql+aiomysql://"
                f"{settings.db_host}:{settings.db_port}/"
                f"{settings.db_name}?"
                f"user={settings.db_user}"
                f"&password={settings.db_password}")


engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
