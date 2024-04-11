from config import ma
from group_members.models import GroupMember
from marshmallow import fields


class GroupMemberSchema(ma.SQLAlchemyAutoSchema):
    account = fields.Int()
    group = fields.Int()

    class Meta:
        model = GroupMember
        fields = ("id", "account", "group", "created_at")


group_member_schema = GroupMemberSchema()
group_member_many_schema = GroupMemberSchema(many=True)
