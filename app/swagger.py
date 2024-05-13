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
            "/group-members": {
                "get": {
                    "summary": "Get all group members",
                    "responses": {
                        "200": {"description": "List of group members"}
                    },
                },
                "post": {
                    "summary": "Create a new group members",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "email": {
                                        "type": "string",
                                        "format": "email",
                                    },
                                    "group": {"type": "integer"},
                                },
                            },
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Group member created successfully"
                        }
                    },
                },
            },
            "/group-members/{group_member_id}": {
                "get": {
                    "summary": "Get a product by ID",
                    "parameters": [
                        {
                            "name": "group_member_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "200": {"description": "Group member details"},
                        "404": {"description": "Group member not found"},
                    },
                },
                "put": {
                    "summary": "Update a group member by ID",
                    "parameters": [
                        {
                            "name": "group_member_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        },
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/GroupMember"},
                        },
                    ],
                    "responses": {
                        "200": {
                            "description": "Group member updated successfully"
                        },
                        "404": {"description": "Group member not found"},
                    },
                },
                "delete": {
                    "summary": "Delete a group member by ID",
                    "parameters": [
                        {
                            "name": "group_member_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "204": {
                            "description": "Group member deleted successfully"
                        },
                        "404": {"description": "Group member not found"},
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
            "/transaction": {
                "get": {
                    "summary": "Get all transactions",
                    "responses": {
                        "200": {"description": "List of transaction"}
                    },
                },
                "post": {
                    "summary": "Create a new transaction",
                    "parameters": [
                        {
                            "name": "body",
                            "in": "body",
                            "required": True,
                            "schema": {"$ref": "#/definitions/Transaction"},
                        }
                    ],
                    "responses": {
                        "201": {
                            "description": "Transaction created successfully"
                        }
                    },
                },
            },
            "/transaction/{transaction_id}": {
                "get": {
                    "summary": "Get a Transaction by ID",
                    "parameters": [
                        {
                            "name": "transaction_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "200": {"description": "Transaction details"},
                        "404": {"description": "Transaction not found"},
                    },
                },
                "put": {
                    "summary": "Update a Transaction by ID",
                    "parameters": [
                        {
                            "name": "transaction_id",
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
                                    "amount": {"type": "number"},
                                    "description": {"type": "string"},
                                    "update_at": {
                                        "type": "string",
                                        "format": "date-time",
                                    },
                                },
                            },
                        },
                    ],
                    "responses": {
                        "200": {
                            "description": "Transaction updated successfully"
                        },
                        "404": {"description": "Transaction not found"},
                    },
                },
                "delete": {
                    "summary": "Delete a Transaction by ID",
                    "parameters": [
                        {
                            "name": "transaction_id",
                            "in": "path",
                            "required": True,
                            "type": "integer",
                        }
                    ],
                    "responses": {
                        "204": {
                            "description": "Transaction deleted successfully"
                        },
                        "404": {"description": "Transaction not found"},
                    },
                },
            },
            "/user-info": {
                "get": {
                    "summary": "Get user information",
                    "responses": {"200": {"description": "User information"}},
                },
            },
        },
        "definitions": {
            "GroupMember": {
                "type": "object",
                "properties": {
                    "account": {"type": "number"},
                    "group": {"type": "number"},
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
            "Transaction": {
                "type": "object",
                "properties": {
                    "amount": {"type": "number"},
                    "description": {"type": "string"},
                    "update_at": {"type": "string", "format": "date-time"},
                    "group": {"type": "number"},
                    "account": {"type": "number"},
                },
            },
        },
    }
    return jsonify(swagger)
