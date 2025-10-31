from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.product import ProductRepository
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse, CartItemResponse


class CartService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)

    def add_to_cart(self, cart_data: dict[int, int], item: CartItemCreate) -> dict[int, int]:
        product = self.product_repository.get_by_id(item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product with id={item.product_id} not found'
            )

        if item.product_id in cart_data:
            cart_data[item.product_id] += item.quantity
        else:
            cart_data[item.product_id] = item.quantity

        return cart_data

    @staticmethod
    def update_cart_item(cart_data: dict[int, int], item: CartItemUpdate) -> dict[int, int]:
        if item.product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product with id={item.product_id} not found in cart'
            )

        cart_data[item.product_id] = item.quantity
        return cart_data

    @staticmethod
    def remove_from_cart(cart_data: dict[int, int], product_id: int) -> dict[int, int]:
        if product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product with id={product_id} not found in cart'
            )

        del cart_data[product_id]
        return cart_data

    def get_cart_details(self, cart_data: dict[int, int]) -> CartResponse:
        if not cart_data:
            return CartResponse(items=[], total=0.0, items_count=0)

        product_ids = list(cart_data.keys())
        products = self.product_repository.get_multiple_by_ids(product_ids)
        products_dict = {product.id: product for product in products}

        cart_items = []
        total_price = 0.0
        total_items = 0

        for product_id, quantity in cart_data.items():
            if product_id in products_dict:
                product = products_dict[product_id]
                subtotal = product.price * quantity

                cart_item = CartItemResponse(
                    product_id=product.id,
                    name=product.name,
                    quantity=quantity,
                    price=product.price,
                    subtotal=subtotal,
                    image_url=product.image_url,
                )

                cart_items.append(cart_item)
                total_price += subtotal
                total_items += quantity

        return CartResponse(
            items=cart_items,
            total=round(total_price),
            items_count=total_items,
        )