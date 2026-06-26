# Stim-Lis-Arb

An asynchronous event-driven arbitrage and statistical analysis system for digital assets (Steam Market & Lis-Skins).

## Architecture Layout
- **analytics_service**: Data Pipeline & Market Intelligence Engine.
- **trading_bot**: Real-time event-driven trading execution core via WebSockets.
- **backend_service**: Interface layer and Telegram notification bot.

## Tech Stack
- **Language**: Python (Asyncio, aiohttp)
- **Database**: Postgresql, SqlAlchemy ORM, Alembic (migrations)
- **Data Science**: Pandas, NumPy, Scipy
- **Infrastructure**: Docker, Docker Compose
