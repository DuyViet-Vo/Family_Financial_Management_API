from config import ma
from groups.models import Group


class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group


group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)
