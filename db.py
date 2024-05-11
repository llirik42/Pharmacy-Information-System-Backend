from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from settings import settings

async_engine = create_async_engine(url=settings.db_url, echo=True)
new_session = async_sessionmaker(autoflush=False, bind=async_engine)
