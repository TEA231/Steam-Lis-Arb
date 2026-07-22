import os
from dotenv import load_dotenv

load_dotenv(".env.local")

# Lisskins API
API_KEY: str = os.getenv("LISKINS_API_KEY", "")
API_URL: str = "https://api.lis-skins.com/v1"

# Парсинг
BATCH_SIZE: int = 200           # скинов за один запрос
PARSE_INTERVAL: int = 1800      # секунд между парсингами (30 минут)

MINIMUM_PRICE_LS: int = 0       # минимальная цена скина Lisskins -> Steam
MAXIMUM_PRICE_LS: int = 2000    # максимальная цена скина Lisskins -> Steam

# База данных (дублируем для удобства, основной источник — engine.py)
DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "sqlite+aiosqlite:///./app.db",
)