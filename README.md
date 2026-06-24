# Stim-Lis-Arb

An asynchronous event-driven arbitrage and statistical analysis system for digital assets (Steam Market & Lis-Skins).

## Architecture Layout
- **parser_service**: A standalone service for batch sampling and aggregation of asset prices.
- **trading_bot**: Real-time event-driven trading execution core via WebSockets.
- **analytics**: Mathematical research module for liquidity scoring, MAD, and outlier filtration.
- **backend_service**: Interface layer and Telegram notification bot.

## Tech Stack
- **Language**: Python (Asyncio, aiohttp)
- **Database**: Postgresql, SqlAlchemy ORM, Alembic (migrations)
- **Data Science**: Pandas, NumPy, Scipy
- **Infrastructure**: Docker, Docker Compose
