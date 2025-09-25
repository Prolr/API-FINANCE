from typing import Any, List
import logging
from crud.Crud_Category import category_crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.request import RequestClient
from api import crud, models, schemas
from api import deps
from schemas.schema_category import CategoryInBase, CategoryUpdate, CategoryCreate

router = APIRouter()
logger = logging.getLogger(__name__)

# BUSCAR CATEGORIA


@router.get("/get", description='Buscar Categoria', response_model=List[CategoryInBase])
async def read_category(
        db: AsyncSession = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:

    logger.info("Consultando Category")
    category_list = await category_crud.get_multi(db=db, skip=skip, limit=limit,)

    return category_list

# BUSCA CATEGORIA PELO  " ID "


@router.get("/GetId/{id}", response_model=CategoryInBase)
async def especific_category(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,

) -> Any:

    category_id_list = await category_crud.get(db=db, id=id)

    return category_id_list

# CRIAR DADOS


@router.post("/post", response_model=CategoryInBase)
async def create_category(
        *,
        db: AsyncSession = Depends(deps.get_db),
        category_in: CategoryCreate,

) -> Any:

    category_post = await category_crud.create(db=db, obj_in=category_in)
    return category_post


# DELETAR CATEGORIA

@router.delete(path="/{id}", response_model=CategoryInBase)
async def delete_category(
        *,
        db: AsyncSession = Depends(deps.get_db),
        id: int,
) -> Any:
    """
    Delete an item.
    """
    category_delete = await category_crud.get(db=db, id=id)

    if not category_delete:

        raise HTTPException(status_code=404, detail="Category not found")
    category_delete = await category_crud.remove(db=db, id=id)

    return category_delete

# ATUALIZAR CATEGORIA


@router.put("/put/{id}", response_model=CategoryInBase)
async def put_category(
    *,
    db: AsyncSession = Depends(deps.get_db),
    category_update: CategoryUpdate,
    id: int,


) -> Any:
    busc_id = await category_crud.get(db=db, id=id)
    update_category = await category_crud.update(db=db, db_obj=busc_id, obj_in=category_update)

    return update_category
