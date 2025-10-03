

# 	transaction.py → Transações financeiras (receitas/despesas).

# faze uma tabela de transações


from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base
from datetime import datetime


class Transaction(Base):
    __tablename__ = "finance_rafa_TB_Transactions"

    id = Column(Integer, primary_key=True, index=True)

    description = Column(String, nullable=True)

    amount = Column(Float, nullable=False)  # valor da transação

    # "income" ou "expense" # | "Receita" ou "Dispesas"
    type = Column(String, nullable=False)

    date = Column(DateTime, default=datetime.utcnow)

    # Relacionamento com Category
    category_id = Column(Integer, ForeignKey(
        "finance_rafa_TB_Categories.id"), nullable=False)

    category = relationship("Category", back_populates="transactions")

    # Relacionamento com User (se já tiver user model)
    user_id = Column(ForeignKey("finance_rafa_TB_Users.id"), nullable=False)
    # relação com user inversqa
    user = relationship("User", back_populates="transactions")
