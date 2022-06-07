from app import app
from flask import json
from flask import request

from models.user import User


def create():
    body = request.json

    user = User()
    user = user.save(
        name=body['name'],
        email=body['email'],
        password=body['password'],
    )
    print('Controller -> Save user:')
    print(user)

    users = User()
    users = users.save_bulk(
        list=[
            {
                'name': body['name'],
                'email': body['email'],
                'password': body['password'],
            },
            {
                'name': body['name'],
                'email': body['email'],
                'password': body['password'],
            },
            {
                'name': body['name'],
                'email': body['email'],
                'password': body['password'],
            },
            {
                'name': body['name'],
                'email': body['email'],
                'password': body['password'],
            },
        ],
    )
    print('Controller -> Save users:')
    print(users)

    response = app.response_class(
        response=json.dumps({
            'body': body,
            'data': {
                'name': 'John',
                'age': 30
            },
            'message': 'User added',
        }),
        status=200,
        mimetype='application/json'
    )
    return response
