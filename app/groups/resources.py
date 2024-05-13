from config import db
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from groups.models import Group
from groups.schemas import group_schema, groups_schema
from users.models import User
from users.schemas import user_schema


class GroupResource(Resource):
    @jwt_required()
    def get(self):
        groups = Group.query.all()
        serialized_groups = []
        for group in groups:
            user = User.query.get(group.user_create)
            user_info = user_schema.dump(user)
            group_data = group_schema.dump(group)
            group_data["user_create"] = user_info
            serialized_groups.append(group_data)
        return serialized_groups

    @jwt_required()
    def post(self):
        group_name = request.json["group_name"]
        user_create = request.json["user_create"]
        new_group = Group(group_name=group_name, user_create=user_create)
        db.session.add(new_group)
        db.session.commit()
        return group_schema.dump(new_group), 201


class GroupResourceID(Resource):
    @jwt_required()
    def get(self, group_id):
        group = Group.query.get(group_id)
        if group:
            user = User.query.get(group.user_create)
            user_info = user_schema.dump(user)
            # Add user information to the group data
            group_data = group_schema.dump(group)
            group_data["user_create"] = user_info
            return group_data
        else:
            abort(404, message="Group not found")

    @jwt_required()
    def put(self, group_id):
        group = Group.query.get(group_id)
        if group:
            group.group_name = request.json["group_name"]
            db.session.commit()
            return group_schema.dump(group)
        else:
            abort(404, message="Group not found")

    @jwt_required()
    def delete(self, group_id):
        group = Group.query.get(group_id)
        if group:
            db.session.delete(group)
            db.session.commit()
            return "", 204
        else:
            abort(404, message="Group not found")
