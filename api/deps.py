import logging
from typing import AsyncGenerator, Generator

from db.session import SessionLocal_212
from db.session import SessionLocal_211
from db.session import SessionLocal_psql


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


# Alias para não quebrar os endpoints que usam `Depends(get_db)`
get_db = get_db_psql
