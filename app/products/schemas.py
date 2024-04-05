from config import ma
from products.models import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
