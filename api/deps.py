from typing import AsyncGenerator, Generator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db.session import SessionLocal_psql, SessionLocal_212, SessionLocal_211


async def get_db_psql() -> AsyncGenerator:
    async with SessionLocal_psql() as db:
        yield db


def get_db_211() -> Generator:
    try:
        db = SessionLocal_211()
        yield db
    finally:
        db.close()


def get_db_212() -> Generator:
    try:
        db = SessionLocal_212()
        yield db
    finally:
        db.close()


get_db = get_db_psql
