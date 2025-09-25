

# 	category.py → Operações de categorias.


from crud.baseAsync import CRUDBase
from models.model_category import Category
from schemas.schema_category import CategoryCreate, CategoryUpdate


class CRUDItem(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category_crud = CRUDItem(Category)
