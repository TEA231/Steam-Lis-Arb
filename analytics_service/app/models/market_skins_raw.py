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
    title: Mapped[str] = mapped_column(String, nullable=False)
    price_mean: Mapped[float] = mapped_column(Float, nullable=False)
    price_std: Mapped[float] = mapped_column(Float, nullable=False)
    avg_qty: Mapped[float] = mapped_column(Float, nullable=False)
    parsed_date: Mapped[date] = mapped_column(Date, nullable=False)