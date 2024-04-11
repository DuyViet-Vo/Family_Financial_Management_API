from flask_restful import Api
from groups.resources import GroupResource, GroupResourceID
from products.resources import ProductResource
from users.resources import LoginResource, UserResource


def create_routes(api):
    # Add resources
    api.add_resource(
        ProductResource, "/products", "/products/<int:product_id>"
    ),
    api.add_resource(UserResource, "/register"),
    api.add_resource(LoginResource, "/login")
    api.add_resource(GroupResource, "/groups"),
    api.add_resource(GroupResourceID, "/groups/<int:group_id>"),
