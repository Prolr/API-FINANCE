from fastapi import APIRouter

from api.api_v1.endpoints import category
from api.api_v1.endpoints import report
from api.api_v1.endpoints import transaction
from api.api_v1.endpoints import user

api_router = APIRouter()
api_router.include_router(
    category.router, prefix="/category", tags=["category"])

api_router.include_router(report.router, prefix="/report", tags=["report"])

api_router.include_router(
    transaction.router, prefix="/transaction", tags=["transaction"])

api_router.include_router(user.router, prefix="/user", tags=["user"])
