from config import db
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from groups.models import Group
from groups.schemas import group_schema, groups_schema

from flask import request


class GroupResource(Resource):
    @jwt_required()
    def get(self, group_id=None):
        if group_id:
            group = Group.query.get(group_id)
            if group:
                return group_schema.dump(group)
            else:
                abort(404, message="Product not found")
        else:
            products = Group.query.all()
            return groups_schema.dump(products)

    @jwt_required()
    def post(self):
        group_name = request.json["group_name"]
        user_create = request.json["user_create"]
        new_group = Group(group_name=group_name, user_create=user_create)
        db.session.add(new_group)
        db.session.commit()
        return group_schema.dump(new_group), 201
