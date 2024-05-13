from config import db
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort
from group_members.models import GroupMember
from group_members.schemas import group_member_many_schema, group_member_schema
from users.models import User


class GroupMemberResource(Resource):
    @jwt_required()
    def get(self):
        group = GroupMember.query.all()
        return group_member_many_schema.dump(group)

    @jwt_required()
    def post(self):
        email = request.json["email"]
        group = request.json["group"]
        user = User.query.filter_by(email=email).first()
        if user is None:
            return {"message": "User does not exist"}, 404
        new_group_member = GroupMember(account=user.id, group=group)
        db.session.add(new_group_member)
        db.session.commit()
        return group_member_schema.dump(new_group_member), 201


class GroupMemberResourceID(Resource):
    @jwt_required()
    def get(self, group_member_id):
        group_member = GroupMember.query.get(group_member_id)
        if group_member:
            return group_member_schema.dump(group_member)
        else:
            abort(404, message="Group member not found")

    @jwt_required()
    def put(self, group_member_id):
        group_member = GroupMember.query.get(group_member_id)
        if group_member:
            group_member.account = request.json["account"]
            group_member.group = request.json["group"]
            db.session.commit()
            return group_member_schema.dump(group_member)
        else:
            abort(404, message="Group member not found")

    @jwt_required()
    def delete(self, group_member_id):
        group_member = GroupMember.query.get(group_member_id)
        if group_member:
            db.session.delete(group_member)
            db.session.commit()
            return "", 204
        else:
            abort(404, message="Group member not found")
