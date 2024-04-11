from flask import jsonify


def swagger_json():
    swagger = {
        "swagger": "2.0",
        "info": {
            "title": "Family Financial Management API",
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
            "/register": {
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
            "/groups": {
                "get": {
                    "summary": "Get all groups",
                    "responses": {"200": {"description": "List of groups"}},
                },
                "post": {
                    "summary": "Create a new product",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/Group"},
                        }
                    ],
                    "responses": {
                        "201": {"description": "Group created successfully"}
                    },
                },
            },
            "/groups/{group_id}": {
                "get": {
                    "summary": "Get a Group by ID",
                    "parameters": [
                        {
                            "name": "group_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "200": {"description": "Group details"},
                        "404": {"description": "Group not found"},
                    },
                },
                "put": {
                    "summary": "Update a group by ID",
                    "parameters": [
                        {
                            "name": "group_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        },
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "group_name": {"type": "string"},
                                },
                            },
                        },
                    ],
                    "responses": {
                        "200": {"description": "Group updated successfully"},
                        "404": {"description": "Group not found"},
                    },
                },
                "delete": {
                    "summary": "Delete a group by ID",
                    "parameters": [
                        {
                            "name": "group_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "204": {"description": "Group deleted successfully"},
                        "404": {"description": "Group not found"},
                    },
                },
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
            "Group": {
                "type": "object",
                "properties": {
                    "group_name": {"type": "string"},
                    "user_create": {"type": "number"},
                },
            },
        },
    }
    return jsonify(swagger)
