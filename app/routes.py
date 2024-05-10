from flask_restful import Api
from group_members.resources import GroupMemberResource, GroupMemberResourceID
from groups.resources import GroupResource, GroupResourceID
from transactions.resources import TransactionsResource, TransactionsResourceID
from users.resources import LoginResource, UserInfoResource, UserResource


def create_routes(api):
    # Add resources
    api.add_resource(UserResource, "/register"),
    api.add_resource(LoginResource, "/login")
    api.add_resource(GroupResource, "/groups"),
    api.add_resource(GroupResourceID, "/groups/<int:group_id>"),
    api.add_resource(GroupMemberResource, "/group-members"),
    api.add_resource(
        GroupMemberResourceID, "/group-members/<int:group_member_id>"
    ),
    api.add_resource(TransactionsResource, "/transaction"),
    api.add_resource(
        TransactionsResourceID, "/transaction/<int:transaction_id>"
    ),
    api.add_resource(UserInfoResource, "/user-info"),
