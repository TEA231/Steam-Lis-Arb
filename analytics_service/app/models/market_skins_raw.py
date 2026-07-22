from datetime import date
from sqlalchemy import (
    String,
    Integer,
    Float,
    Date
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class MarketSkinsRaw(Base):
    __tablename__ = "market_skins_raw"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)       # Название скина
    price_mean: Mapped[float] = mapped_column(Float, nullable=False) # Средняя цена
    price_std: Mapped[float] = mapped_column(Float, nullable=False)  # Среднее отклонение цены
    avg_qty: Mapped[float] = mapped_column(Float, nullable=False)    # Среднее количество экземпляров
    parsed_date: Mapped[date] = mapped_column(Date, nullable=False)  # День парсинга

    # Агрегированные данные по каждому дню для каждого скина