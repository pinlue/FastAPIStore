from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, func

from app.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Product(id={self.id}, name="{self.name}"'