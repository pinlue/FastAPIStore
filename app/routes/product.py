from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductListResponse, ProductResponse
from app.services.product import ProductService

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)


@router.get(
    '',
    status_code=status.HTTP_200_OK
)
def get_products(db: Session = Depends(get_db)) -> ProductListResponse:
    service = ProductService(db)
    return service.get_all_products()


@router.get(
    '/{product_id}',
    status_code=status.HTTP_200_OK
)
def get_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    service = ProductService(db)
    return service.get_product_by_id(product_id)


@router.get(
    '/categories/{category_id}',
    status_code=status.HTTP_200_OK
)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)) -> ProductListResponse:
    service = ProductService(db)
    return service.get_products_by_category_id(category_id)