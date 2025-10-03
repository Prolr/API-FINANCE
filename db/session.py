from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from core.config import settings
from contextlib import asynccontextmanager

# PostgreSQL (assíncrono)
engine_psql = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI_PG),
    pool_pre_ping=True,
    future=True,
)

SessionLocal_psql = sessionmaker(
    bind=engine_psql,
    class_=AsyncSession,
    expire_on_commit=False,
)


# SQL Server 212 (síncrono)
engine_212 = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI_212),
    pool_pre_ping=True
)
SQLAlchemyInstrumentor().instrument(engine=engine_212)

SessionLocal_212 = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_212
)


# SQL Server 211 (síncrono)
engine_211 = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI_211),
    pool_pre_ping=True
)
SQLAlchemyInstrumentor().instrument(engine=engine_211)

SessionLocal_211 = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_211
)


async def get_db():
    db = SessionLocal_psql()
    try:
        yield db
    finally:
        await db.close()
