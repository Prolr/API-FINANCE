from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
from api import deps
from core.security import get_current_user, verify_password, create_access_token
from core.config import settings
from crud.Crud_User import user_crud
from schemas.schema_user import Token, UserBaseLogin

import db
from models.model_user import User


router = APIRouter()


@router.post("/generate_token", response_model=Token)
async def login(
        form_data: UserBaseLogin,
        db: AsyncSession = Depends(deps.get_db)
) -> Any:
    print("Username recebido:", form_data.username)
    print("Password recebido:", form_data.password)

    user = await user_crud.get_by_email(db=db, email=form_data.username)
    print("User encontrado:", user)

    if not user or not verify_password(form_data.password, user.hashed_password):
        print("Falhou: user is None ou senha inválida")
        raise HTTPException(status_code=401, detail="EMAIL ou SENHA inválidos")

    expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    create_token = create_access_token(
        data={"sub": user.email},
        expires_delta=expires
    )
    return {"access_token": create_token, "token_type": "bearer"}


@router.get("/validate_token")
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user
