from fastapi import APIRouter, Depends

from api.api_v1.endpoints import category, login
from api.api_v1.endpoints import report
from api.api_v1.endpoints import transaction
from api.api_v1.endpoints import user
from core.security import get_current_user

api_router = APIRouter()


api_router.include_router(
    category.router, prefix="/category", tags=["category"], dependencies=[Depends(get_current_user)])

api_router.include_router(report.router, prefix="/report",
                          tags=["report"], dependencies=[Depends(get_current_user)])

api_router.include_router(transaction.router, prefix="/transaction",
                          tags=["transaction"], dependencies=[Depends(get_current_user)])

api_router.include_router(user.router, prefix="/user",
                          tags=["user"], dependencies=[Depends(get_current_user)])

api_router.include_router(login.router, prefix="/auth", tags=[
                          "auth"])  # <-- inclui o router de login
