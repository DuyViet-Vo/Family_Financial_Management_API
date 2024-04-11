from config import ma
from groups.models import Group
from marshmallow import fields
from users.schemas import UserSchema


class GroupSchema(ma.SQLAlchemyAutoSchema):
    user_create = fields.Int()

    class Meta:
        model = Group
        fields = ("id", "group_name", "user_create", "created_at")


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
