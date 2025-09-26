

# security.py → Funções de autenticação e geração de tokens(JWT).
import secrets
from core.config import Settings
from pydantic_settings import BaseSettings
from passlib.context import CryptContext
from pytz import timezone
from typing import Optional, List
from datetime import datetime, timedelta
from fastapi.security import OAuth2AuthorizationCodeBearer
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt
import models.model_user import Base
from core.config import settings
from core.config import verificar_senha
from pydantic import EmailStr
from models.model_user import User


CRIPTO = CryptContext(schemas=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, has_senha: str) -> bool:
    pass

    return CRIPTO.verify(senha, has_senha)


def gerar_hash_senha(senha: str) -> str:

    return CRIPTO.hash(senha)


# Verificação

oauth2_schemas = OAuth2AuthorizationCodeBearer(
    tokenUrl="{setting.API_V1_STR}/usuarios/login"
)


async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[User]:
    async with db as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)
        usuario = User = result.scalar().unique().one_or_none()

    if not usuario:
        return None

    if not verificar_senha(senha, usuario.senha):
        return None
    return usuario


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone('America/São Paulo')
    expira = datetime.now(tz=sp) + tempo_vida

    payload['type'] = tipo_token
    payload['exp'] = expira
    payload['iat'] = datetime.now(tz=sp)
    payload['sub'] = str(sub)
    return jwt.encode(payload, settings.JWT.SECRETS, algorithm=settings.ALGORITHM)


def criar_token_acesso(subs: str) -> str:
    '''
    https://jwt.io
    '''
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        subs=subs

    )
