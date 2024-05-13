from config import ma
from groups.models import Group


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        fields = ("id", "group_name", "user_create", "created_at")


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
