from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from app.models import Product
from app.repositories.base import GenericRepository
from app.schemas.product import ProductCreate


class ProductRepository(GenericRepository[Product, ProductCreate]):
    def __init__(self, db: Session):
        super().__init__(db, Product)

    def get_by_category_id(self, category_id: int) -> list[Product]:
        return list(self.db.scalars(
            select(Product)
            .options(joinedload(Product.category))
            .where(Product.category_id == category_id)
        ).all())

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.scalar(
            select(Product)
            .options(joinedload(Product.category))
            .where(Product.id == product_id)
        )

    def get_multiple_by_ids(self, product_ids: list[int]) -> list[Product]:
        return list(self.db.scalars(
            select(Product)
            .options(joinedload(Product.category))
            .where(Product.id.in_(product_ids))
        ).all())
