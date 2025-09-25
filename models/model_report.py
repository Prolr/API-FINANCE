

# 	report.py → Relatórios consolidados (ex: gastos por mês, saldo).


# faze uma tabela de relatorio


from sqlalchemy import Column, Integer, Float, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from db.base_class import Base


class Report(Base):
    __tablename__ = "finance_rafa_TB_Reports"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    total_income = Column(Float, default=0.0)   # soma das receitas
    total_expense = Column(Float, default=0.0)  # soma das despesas
    balance = Column(Float, default=0.0)        # saldo final

    # chave estrangeira obrigatória
    user_id = Column(Integer, ForeignKey(
        "finance_rafa_TB_Users.id"), nullable=False)

    # Relação inversa com report
    user = relationship("User", back_populates="reports")
