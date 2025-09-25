

# 	user.py → Usuários (login, senha, email).


# faze uma tabela de usuario


from sqlalchemy import Column, Integer, String
from db.base_class import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "finance_rafa_TB_Users"   # nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    transactions = relationship("Transaction", back_populates="user")
    reports = relationship("Report", back_populates="user")
