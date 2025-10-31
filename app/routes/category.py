from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.category import CategoryResponse
from ..services.category import CategoryService

router = APIRouter(
    prefix='/api/categories',
    tags=['categories'],
)


@router.get(
    '',
    status_code=status.HTTP_200_OK,
)
def get_categories(db: Session = Depends(get_db)) -> list[CategoryResponse]:
    service = CategoryService(db)
    return service.get_all_categories()


@router.get(
    '/{category_id}',
    status_code=status.HTTP_200_OK,
)
def get_category(category_id: int, db: Session = Depends(get_db)) -> CategoryResponse:
    service = CategoryService(db)
    return service.get_category_by_id(category_id)
