from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from api import deps
from core.security import get_current_user, verify_password, create_access_token, get_db, verificar_senha, gerar_hash_senha
from core.config import settings
from crud.Crud_User import User_Crud
import db
from models.model_user import User, hashed_password
from schemas.schema_user import UserCreate


router = APIRouter()


@router.get("/financeiro")
async def dados_financeiros(user: User = Depends(get_current_user)):
    return {"msg": f"Acesso autorizado para {user.email}"}
