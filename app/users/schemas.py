from config import ma
from users.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "username", "email", "created_at")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
