from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.cart import AddToCartRequest, CartItemCreate, CartResponse, UpdateCartRequest, CartItemUpdate, \
    RemoveFromCartRequest
from app.services.cart import CartService

router = APIRouter(
    prefix='/api/carts',
    tags=['cart']
)

#ToDo
@router.post(
    '/items',
    status_code=status.HTTP_200_OK,
)
def add_to_cart(request: AddToCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemCreate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.add_to_cart(request.cart, item)
    return {'cart': updated_cart}


@router.post(
    '',
    status_code=status.HTTP_200_OK,
)
def get_cart(cart_data: dict[int, int], db: Session = Depends(get_db)) -> CartResponse:
    service = CartService(db)
    return service.get_cart_details(cart_data)

#ToDo
@router.put(
    '',
    status_code=status.HTTP_200_OK,
)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    item = CartItemUpdate(product_id=request.product_id, quantity=request.quantity)
    updated_cart = service.update_cart_item(request.cart, item)
    return {'cart': updated_cart}

#ToDo
@router.delete(
    '/items/{product_id}',
    status_code=status.HTTP_200_OK,
)
def remove_from_cart(product_id: int, request: RemoveFromCartRequest, db: Session = Depends(get_db)):
    service = CartService(db)
    updated_cart = service.remove_from_cart(request.cart, product_id)
    return {'cart': updated_cart}
