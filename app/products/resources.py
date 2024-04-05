from config import db
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from products.models import Product
from products.schemas import product_schema, products_schema

from flask import request


class ProductResource(Resource):
    @jwt_required()  # Yêu cầu xác thực token cho tất cả các phương thức trong class này
    def get(self, product_id=None):
        if product_id:
            product = Product.query.get(product_id)
            if product:
                return product_schema.dump(product)
            else:
                abort(404, message="Product not found")
        else:
            products = Product.query.all()
            return products_schema.dump(products)

    @jwt_required()  # Yêu cầu xác thực token cho tất cả các phương thức trong class này
    def post(self):
        name = request.json["name"]
        price = request.json["price"]
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product), 201

    @jwt_required()  # Yêu cầu xác thực token cho tất cả các phương thức trong class này
    def put(self, product_id):
        product = Product.query.get(product_id)
        if product:
            product.name = request.json["name"]
            product.price = request.json["price"]
            db.session.commit()
            return product_schema.dump(product)
        else:
            abort(404, message="Product not found")

    @jwt_required()  # Yêu cầu xác thực token cho tất cả các phương thức trong class này
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return "", 204
        else:
            abort(404, message="Product not found")
