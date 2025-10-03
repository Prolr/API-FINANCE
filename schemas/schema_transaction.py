

# 	transaction.py → Esquema de transações.

from datetime import datetime, date
from typing import Optional, Literal
from pydantic import BaseModel, Field


class TransactionBase(BaseModel):

    description: Optional[str] = None
    amount: float
    user_id: int
    category_id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    type: str


class TransactionInBase(TransactionBase):
    id: int
    date: datetime


class Transaction(TransactionInBase):
    pass
