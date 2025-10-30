from pydantic import BaseModel, Field, ConfigDict


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description='Category name')
    slug: str = Field(..., min_length=3, max_length=100, description='URL-friendly category name')

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique category identifier')

    model_config = ConfigDict(from_attributes=True)