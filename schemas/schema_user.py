

# 	user.py → Esquema de usuário (registro/login/retorno).


from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    email: str
    hashed_password: str
    cpf: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInBase(UserBase):
    id: int
    hashed_password: str


class User(UserInBase):
    pass
