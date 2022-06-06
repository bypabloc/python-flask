from controllers.user.create import create as create_user
from controllers.user.list import list as list_users


print("Imported controllers: %s" % ", ".join(["create", "list"]))


class UserController:
    def __init__(self):
        print("UserController initialized")
        self.create = create_user
        self.list = list_users
