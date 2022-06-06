from app import app
from app import json
from app import request


def create():
    body = request.json

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
