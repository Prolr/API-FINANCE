from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.request import RequestClient
from api import crud, models, schemas
from api import deps
from crud.Crud_Transaction import Transaction_Crud
from crud.Crud_Report import report_crud
from schemas.schema_transaction import TransactionInBase, TransactionUpdate, TransactionCreate

from typing import Any, List, Literal
import logging
from schemas.schema_report import ReportInBase, ReportUpdate, ReportCreate

router = APIRouter()
logger = logging.getLogger(__name__)

# BUSCAR CATEGORIA


@router.get("/get", response_model=List[TransactionInBase])
async def read_transaction(
        db: AsyncSession = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:

    logger.info("Consultando Relatorio")
    transaction_list = await Transaction_Crud.get_multi(db=db, skip=skip, limit=limit,)

    return transaction_list

# BUSCA CATEGORIA PELO  " ID "


@router.get("/GetId/{id}", response_model=TransactionInBase)
async def especific_transaction(
    *,
    db: AsyncSession = Depends(deps.get_db),
    id: int,

) -> Any:

    transaction_id_list = await Transaction_Crud.get(db=db, id=id)

    return transaction_id_list

# CRIAR DADOS


@router.post("/post", response_model=ReportInBase,
             description="type = Receita ou Dispesas |"
             " amount= valor da transação", )
async def create_transaction(
        *,
        db: AsyncSession = Depends(deps.get_db),
        transaction_in: TransactionCreate,
        type: Literal["Receita", "Dispesas"]



) -> Any:
    if type == "Dispesas":
        transaction_in.amount = abs(transaction_in.amount)
    elif type == "Receita":
        transaction_in.amount = abs(transaction_in.amount)

    button_type = transaction_in.model_dump()
    button_type["type"] = type

    transaction_create = await Transaction_Crud.create(
        db=db, obj_in=button_type)

    # Buscar relatório existente

    _report = await report_crud.get_first_by_filter(db=db, filterby="user_id", filter=transaction_in.user_id)

    # Caso não exista relatório

    if not _report:
        _total_expense = transaction_create.amount if transaction_create.type == 'Dispesas' else 0
        _total_income = transaction_create.amount if transaction_create.type == 'Receita' else 0

        # Cria um novo relatório no banco com:
        _new_report = ReportCreate(
            user_id=transaction_in.user_id,
            balance=_total_income - _total_expense,
            total_expense=_total_expense,
            total_income=_total_income
        )
        new_report = await report_crud.create(db=db, obj_in=_new_report)
        # Caso já exista relatório
    else:
        _total_expense = _report.total_expense + \
            transaction_create.amount if transaction_create.type == 'Dispesas' else _report.total_expense
        _total_income = _report.total_income + \
            transaction_create.amount if transaction_create.type == 'Receita' else _report.total_income

        # atualiza o relatório já existente
        _new_report = ReportUpdate(
            balance=_total_income-_total_expense,
            total_expense=_total_expense,
            total_income=_total_income
        )
        new_report = await report_crud.update(db=db, obj_in=_new_report, db_obj=_report,)

    return new_report


# ATUALIZAR CATEGORIA


@router.put("/put/{id}", response_model=TransactionInBase)
async def put_transaction(
    *,
    db: AsyncSession = Depends(deps.get_db),
    transaction_update: TransactionUpdate,
    id: int,


) -> Any:
    busc_id = await Transaction_Crud.get(db=db, id=id)
    update_transaction = await Transaction_Crud.update(db=db, db_obj=busc_id, obj_in=transaction_update)

    return update_transaction


# @router.post("/", response_model=TransactionInBase)
# async def post_transaction_1(
#     *,
#     db: AsyncSession = Depends(deps.get_db),
#     transaction_create: TransactionCreate


# ) -> Any:
#     busc = await Transaction_Crud.create(db=db, obj_in=transaction_create)

#     busc_report = await Transaction_Crud.get_first_by_filter(db=db, filterby="user_id", filter=transaction_create.user_id)
#     if not busc_report:
#         busc_dispense = transaction_create.amount if transaction_create.type == "Dispesas" else 0
#         busc_Receita = transaction_create.amount if transaction_create.type == "Receita" else 0

#         _create_report = ReportCreate(
#             user_id=transaction_create.user_id,
#             balance=busc_dispense - busc_Receita,
#             total_expense=busc_Receita,
#             total_income=busc_dispense
#         )

#         create_report = await transaction_create.create(db=db, obj_in=_create_report)

#     else:
#         busc_Receita = busc.busc_Receita + \
#             transaction_create.amount if transaction_create.type == "Receita" else busc_report.busc_Receita
#         busc_dispense = busc.busc_dispense + \
#             transaction_create.amount if transaction_create.type == "Dispesas" else busc_report.busc_dispense

#         _create_report = ReportCreate(
#             user_id=transaction_create.user_id,
#             balance=busc_dispense - busc_Receita,
#             total_expense=busc_Receita,
#             total_income=busc_dispense
#         )
#         create_report = await report_crud.update(db=db, obj_in=create_report, db_obj=_create_report,)
#         return create_report
