

# 	transaction.py → Operações de transações.
from crud.baseAsync import CRUDBase
from models.model_transaction import Transaction
from schemas.schema_transaction import TransactionCreate, TransactionUpdate


class CRUDItem(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    pass


Transaction_Crud = CRUDItem(Transaction)
