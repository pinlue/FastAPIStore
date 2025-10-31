from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class CartItemBase(BaseModel):
    product_id: int = Field(..., description='Product ID')
    quantity: int = Field(..., gt=0, description='Quantity (must be greater than 0)')

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(CartItemBase):
    quantity: int = Field(..., gt=0, description='New quantity (must be greater than 0)')

class CartItemResponse(CartItemBase):
    name: str = Field(..., description='Product name')
    price: float = Field(..., description='Product price')
    subtotal: float = Field(..., description='Total price for this item (price * quantity)')
    image_url: Optional[str] = Field(None, description='Product image URL')

    model_config = ConfigDict(from_attributes=True)

class CartResponse(BaseModel):
    items: list[CartItemResponse] = Field(..., description='List of cart items')
    total: float = Field(..., description='Total cart price')
    items_count: int = Field(..., gt=0, description='Total number of cart items')
#ToDo
class AddToCartRequest(CartItemBase):
    cart: dict[int, int] = {}

class UpdateCartRequest(CartItemBase):
    cart: dict[int, int] = {}

class RemoveFromCartRequest(BaseModel):
    cart: dict[int, int] = {}