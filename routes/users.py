from app import app

import controllers


app.add_url_rule('/users/list', view_func=controllers.UserController.list, methods=['GET'])
app.add_url_rule('/users/create', view_func=controllers.UserController.create, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)
