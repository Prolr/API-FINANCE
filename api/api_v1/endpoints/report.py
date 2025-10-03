from core.security import get_current_user
from crud.Crud_Report import report_crud
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from core.request import RequestClient
from api import crud, models, schemas
from api import deps
from models.model_user import User
from schemas.schema_report import ReportInBase, ReportUpdate, ReportCreate
from typing import Any, List
import logging


router = APIRouter()
logger = logging.getLogger(__name__)

# BUSCAR CATEGORIA


@router.get("/", response_model=List[ReportInBase])
async def read_report(
        db: AsyncSession = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:

    logger.info("Consultando Relatorio")
    report_list = await report_crud.get_multi(db=db, skip=skip, limit=limit,)

    return report_list

# BUSCA CATEGORIA PELO  " ID "


@router.get("/{id}", response_model=ReportInBase)
async def especific_report(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,

) -> Any:

    report_id_list = await report_crud.get(db=db, id=id)

    return report_id_list

# CRIAR DADOS


@router.post("/", response_model=ReportInBase)
async def create_report(
        *,
        db: AsyncSession = Depends(deps.get_db),
        report_in: ReportCreate,

) -> Any:

    report_create = await report_crud.create(db=db, obj_in=report_in)
    return report_create


# DELETAR CATEGORIA

@router.delete("/{id}", response_model=ReportInBase)
async def delete_report(
        *,
        db: AsyncSession = Depends(deps.get_db),
        id: int,
) -> Any:

    report_delete = await report_crud.get(db=db, id=id)

    if not report_delete:

        raise HTTPException(status_code=404, detail="Relatório não encontrado")
    report_delete = await report_crud.remove(db=db, id=id)

    return report_delete

# ATUALIZAR CATEGORIA


@router.put("/{id}", response_model=ReportInBase)
async def update_report(
    *,
    db: AsyncSession = Depends(deps.get_db),
    report_update: ReportUpdate,
    id: int,


) -> Any:
    busc_report = await report_crud.get(db=db, id=id)

    update_report = await report_crud.update(db=db, db_obj=busc_report, obj_in=report_update)

    return update_report
