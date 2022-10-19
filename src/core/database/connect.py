from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core import config

engine = create_async_engine(config.DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def create_async_connection() -> AsyncSession:
    async with async_session() as connection:
        yield(connection)