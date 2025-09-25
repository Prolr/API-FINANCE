

# 	report.py → Esquema de relatórios.


from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class ReportBase(BaseModel):

    total_income: float   # soma das receitas
    total_expense: float  # soma das despesas
    balance: float        # saldo final


class ReportCreate(ReportBase):
    user_id: int


class ReportUpdate(ReportBase):
    pass


class ReportInBase(ReportBase):
    id: int
    created_at: datetime
    user_id: int


class Report(ReportInBase):
    pass
