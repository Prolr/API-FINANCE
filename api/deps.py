import logging
from typing import AsyncGenerator, Generator

from fastapi import HTTPException
from grpc import Status
from requests import Session
from core. import oauth2_schema
from db.session import SessionLocal_212
from db.session import SessionLocal_211
from db.session import SessionLocal_psql
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Asyn
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from models.model_user import User


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


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session() -> AsyncGenerator:
    session: AsyncSession = session

    try:
        yield session
    finally:
        await session.close()


async def get_current_user(
    db: Session = Depends(get_session),
    token: str = Depends(oauth2_schema)

) -> UsuarioModel:
    credential_exception: HTTPException = HTTPException
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ('não foi possivel autenticar sua  credencial'
              headers={"WWWE-Autenticar": "Bearer"},

              )

try:
    payload = jwt.decode(
        token,
        settings.JWT_SECRETS,
        options={"verify_aud ": False}
    )
username: str = payload.get(" sub")
if username is None:
    raise credential_exeption

async with db as session:
    query = select(User).filter(username.id == int(token_data_Username))
