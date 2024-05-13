from config import ma
from group_members.models import GroupMember


class GroupMemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GroupMember
        fields = ("id", "account", "group", "created_at")


group_member_schema = GroupMemberSchema()
group_member_many_schema = GroupMemberSchema(many=True)
