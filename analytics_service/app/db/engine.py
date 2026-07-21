from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from typing import AsyncGenerator

from app.db.base import Base

# Чтение URL из окружения
import os
from dotenv import load_dotenv

load_dotenv(".env.local")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./app.db")

# Асинхронный engine
engine = create_async_engine(DATABASE_URL, echo=False)

# Фабрика асинхронных сессий
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Dependency для получения сессии БД."""
    async with async_session() as session:
        yield session


async def init_db() -> None:
    """Создание всех таблиц (для разработки)."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
