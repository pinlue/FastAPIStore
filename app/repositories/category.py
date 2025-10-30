from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Category
from app.repositories.base import GenericRepository
from app.schemas.category import CategoryCreate


class CategoryRepository(GenericRepository[Category, CategoryCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Category)

    def get_by_slug(self, slug: str) -> Optional[Category]:
        return self.db.scalar(select(Category).where(Category.slug == slug))