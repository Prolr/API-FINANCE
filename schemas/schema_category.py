

# 	category.py → Esquema de categorias.

from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):

    # OUTRA OPÇÃO É USAR DATETIME MAS TERIA QUE FAZER UMA COLUM PARA SERVI YEAR E MONTH

    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryInBase(CategoryBase):
    id: int
    created_at: datetime


class Category(CategoryInBase):
    pass
