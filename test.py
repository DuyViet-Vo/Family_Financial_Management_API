from datetime import datetime, timedelta

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import fields
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Flask, jsonify, request

app = Flask(__name__)
api = Api(app)

# Cấu hình kết nối đến PostgreSQL
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:vdv1810@localhost/test_db_1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "your_secret_key"  # Key bí mật cho mã JWT

# Khởi tạo đối tượng SQLAlchemy
db = SQLAlchemy(app)

# Khởi tạo đối tượng Marshmallow
ma = Marshmallow(app)

# Khởi tạo đối tượng JWTManager
jwt = JWTManager(app)


# Định nghĩa mô hình Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Định nghĩa schema cho serialization và deserialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Định nghĩa schema cho serialization và deserialization
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Đường dẫn Swagger UI
SWAGGER_URL = "/api/docs"
API_URL = "/api/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Product API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Tạo bảng nếu chưa tồn tại
with app.app_context():
    db.create_all()


# Xử lý các yêu cầu về sản phẩm
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


api.add_resource(ProductResource, "/products", "/products/<int:product_id>")


# Xử lý các yêu cầu về người dùng
class UserResource(Resource):
    def post(self):
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]

        # Kiểm tra xem email đã tồn tại trong cơ sở dữ liệu hay chưa
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"message": "Email already exists"}, 400

        # Nếu email chưa tồn tại, thêm người dùng mới vào cơ sở dữ liệu
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201


api.add_resource(UserResource, "/users")


# Endpoint đăng nhập
class LoginResource(Resource):
    def post(self):
        email = request.json.get("email", None)
        password = request.json.get("password", None)

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return {"message": "Invalid username or password"}, 401

        # Tạo token
        access_token = create_access_token(
            identity=email, expires_delta=timedelta(minutes=60)
        )
        return {"access_token": access_token}, 200


api.add_resource(LoginResource, "/login")


@app.route("/api/swagger.json")
def swagger_json():
    swagger = {
        "swagger": "2.0",
        "info": {
            "title": "Test",
            "description": "API for managing products and users",
            "version": "3.0",
        },
        "basePath": "/",
        "schemes": ["http", "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
            }
        },
        "security": [{"Bearer": []}],
        "paths": {
            "/products": {
                "get": {
                    "summary": "Get all products",
                    "responses": {"200": {"description": "List of products"}},
                },
                "post": {
                    "summary": "Create a new product",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/Product"},
                        }
                    ],
                    "responses": {
                        "201": {"description": "Product created successfully"}
                    },
                },
            },
            "/products/{product_id}": {
                "get": {
                    "summary": "Get a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "200": {"description": "Product details"},
                        "404": {"description": "Product not found"},
                    },
                },
                "put": {
                    "summary": "Update a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        },
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/Product"},
                        },
                    ],
                    "responses": {
                        "200": {"description": "Product updated successfully"},
                        "404": {"description": "Product not found"},
                    },
                },
                "delete": {
                    "summary": "Delete a product by ID",
                    "parameters": [
                        {
                            "name": "product_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "204": {"description": "Product deleted successfully"},
                        "404": {"description": "Product not found"},
                    },
                },
            },
            "/users": {
                "post": {
                    "summary": "Register a new user",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/User"},
                        }
                    ],
                    "responses": {
                        "201": {"description": "User registered successfully"},
                        "400": {"description": "Email already exists"},
                    },
                }
            },
            "/login": {
                "post": {
                    "summary": "Login",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/Login"},
                        }
                    ],
                    "responses": {
                        "200": {"description": "Login successful"},
                        "401": {"description": "Invalid username or password"},
                    },
                }
            },
        },
        "definitions": {
            "Product": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "price": {"type": "number"},
                },
            },
            "User": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "email": {"type": "string"},
                },
            },
            "Login": {
                "type": "object",
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                },
            },
        },
    }
    return jsonify(swagger)


if __name__ == "__main__":
    app.run(debug=True)
