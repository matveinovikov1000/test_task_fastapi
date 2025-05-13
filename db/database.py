import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

load_dotenv()

DATABASE_URL = f'postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/{os.getenv("POSTGRES_DB")}'

engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    """Запускает сессию для работы с БД"""
    async with SessionLocal() as session:
        yield session
