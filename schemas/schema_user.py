

# 	user.py → Esquema de usuário (registro/login/retorno).

from utils import valida_cpf
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field, validate_email, validator, EmailStr
from utils import valida_cpf, valida_email
from fastapi import HTTPException, status


class UserBaseLogin(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    cpf: str

    def __init__(self, **data):

        super().__init__(**data)  # inicializa normalmente
        if not valida_cpf(self.cpf):   # chama sua função
            raise ValueError("CPF inválido")

    # valida e-mail
        if not valida_email(self.email):
            raise ValueError("E-mail inválido")


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInBase(UserBase):
    id: int
    hashed_password: str


class User(UserInBase):
    pass
