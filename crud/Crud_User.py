

# 	user.py → Operações de usuários.


from core.security import verify_password, get_password_hash
# 	report.py → Operações de relatórios.
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import get_password_hash
import db
from models.model_user import User
from crud.baseAsync import CRUDBase
from models.model_user import User
from schemas.schema_user import UserCreate, UserUpdate
from utils import valida_cpf, valida_email
from passlib.exc import UnknownHashError


class CRUDItem(CRUDBase[User, UserCreate, UserUpdate]):

    async def get_by_email(self, db: AsyncSession, email: str):
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    async def create(self, db, *, obj_in: UserCreate):

        if not valida_cpf(obj_in.cpf):
            raise HTTPException(status_code=400, detail="CPF inválido")

        if not valida_email(obj_in.email):
            raise HTTPException(status_code=400, detail="EMAIL inválido")

            # criando hash para as senhas do user

        hash_password = get_password_hash(obj_in.password)

        new_user = User(
            email=obj_in.email,
            cpf=obj_in.cpf,
            hashed_password=hash_password,
            name=obj_in.name
        )

        db.add(new_user)
        try:
            await db.commit()
            await db.refresh(new_user)
        except IntegrityError as e:
            await db.rollback()

            if "cpf" in str(e.orig):
                raise HTTPException(
                    status_code=400, detail="CPF INSERIDOS EXISTENTE")

            elif "email" in str(e.orig):
                raise HTTPException(
                    status_code=400, detail="EMAIL INSERIDOS EXISTENTE")

        return new_user


user_crud = CRUDItem(User)
