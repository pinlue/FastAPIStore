from typing import TypeVar, Generic, Type, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session


T = TypeVar("T")
C = TypeVar("C")

class GenericRepository(Generic[T, C]):
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_all(self) -> list[T]:
        return list(self.db.scalars(select(self.model)).all())

    def get_by_id(self, entity_id: int) -> Optional[T]:
        return self.db.get(self.model, entity_id)

    def create(self, entity_data: C) -> T:
        db_entity = self.model(**entity_data.model_dump())
        with self.db.begin():
            self.db.add(db_entity)
        self.db.refresh(db_entity)
        return db_entity