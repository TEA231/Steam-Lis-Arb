from datatime import time
from sqlalchemy import (
    String,
    Integer,
    Float,
    Time
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class MarketSkinsDaily(Base):
    __tablename__ = "market_skins_daily"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    qty: Mapped[int] = mapped_column(Integer, nullable=False)
    parsed_time: Mapped[time] = mapped_column(Time, nullable=False)