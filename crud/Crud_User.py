

# 	user.py → Operações de usuários.


# 	report.py → Operações de relatórios.
from crud.baseAsync import CRUDBase
from models.model_user import User
from schemas.schema_user import UserCreate, UserUpdate


class CRUDItem(CRUDBase[User, UserCreate, UserUpdate]):
    pass


User_Crud = CRUDItem(User)
