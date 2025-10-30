from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schemas.category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=200, description='Product name')
    description: Optional[str] = Field(None, description='Product description')
    price: float = Field(...,gt=0 ,description='Product price(must be greater than 0)')
    category_id: int = Field(...,description='Category id')
    image_url: Optional[str] = Field(None, description='Product image URL')

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description='Unique product identifier')
    created_at: datetime = Field(..., description='Product creation timestamp')
    category: CategoryResponse = Field(..., description='Detailed category information')

    model_config = ConfigDict(from_attributes=True)

class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    total: int = Field(..., description='Total number of products')