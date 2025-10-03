from core.security import get_current_user
from crud.Crud_User import user_crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.request import RequestClient
from api import crud, models, schemas
from api import deps
from schemas.schema_user import UserInBase, UserUpdate, UserCreate, User
from typing import Any, List
import logging


router = APIRouter()
logger = logging.getLogger(__name__)

# BUSCAR CATEGORIA


@router.get("/get", response_model=List[UserInBase])
async def read_user(
        db: AsyncSession = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:

    logger.info("Consultando Relatorio")
    user_list = await user_crud.get_multi(db=db, skip=skip, limit=limit,)

    return user_list

# BUSCA CATEGORIA PELO  " ID "


@router.get("/GetId/{id}", response_model=UserInBase)
async def especific_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,

) -> Any:

    user_id_list = await user_crud.get(db=db, id=id)

    return user_id_list

# CRIAR DADOS


@router.post("/post", response_model=UserInBase)
async def create_user(
        *,
        db: AsyncSession = Depends(deps.get_db),
        category_in: UserCreate,

) -> Any:

    user_create = await user_crud.create(db=db, obj_in=category_in)
    return user_create


# DELETAR CATEGORIA

@router.delete(path="/{id}", response_model=UserInBase)
async def delete_user(
        *,
        db: AsyncSession = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Delete an item.
    """
    user_delete = await user_crud.get(db=db, id=id)

    if not user_delete:

        raise HTTPException(status_code=404, detail="Relatório não encontrado")
    user_delete = await user_crud.remove(db=db, id=id)

    return user_delete

# ATUALIZAR CATEGORIA


@router.put("/put/{id}", response_model=UserInBase)
async def put_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    category_update: UserUpdate,
    id: int,


) -> Any:
    busc_id = await user_crud.get(db=db, id=id)

    update_user = await user_crud.update(db=db, db_obj=busc_id, obj_in=category_update)

    return update_user


@router.get("/me")
async def read_me(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email}
