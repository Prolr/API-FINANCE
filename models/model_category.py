

# 	category.py → Categorias (alimentação, transporte, salário etc.).


# faze uma tabela de categoria


from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from db.base_class import Base


class Category(Base):
    __tablename__ = "finance_rafa_TB_Categories"

    id = Column(Integer, primary_key=True, index=True)
    # alimentação, transporte, salário
    name = Column(String, unique=True, index=True, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relacionamento com Transaction
    transactions = relationship("Transaction", back_populates="category")
