

# security.py → Funções de autenticação e geração de tokens(JWT).

import secrets
from core.config import Settings
from pydantic_settings import BaseSettings
from passlib.context import CryptContext

CRIPTO = CryptContext(schemas=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, has_senha: str) -> bool:
    pass

    return CRIPTO.verify(senha, has_senha)


def gerar_hash_senha(senha: str) -> str:

    return CRIPTO.hash(senha)
