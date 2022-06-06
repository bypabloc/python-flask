from app import app
from app import json
from app import request


def list():
    args = request.args

    per_page = args.get('perpage', 10)
    page = args.get('page', 1)

    response = app.response_class(
        response=json.dumps({
            'data': {
                'list': {
                    'per_page': per_page,
                    'page': page,
                    'data': [
                        {
                            'name': 'John',
                            'age': 30
                        },
                        {
                            'name': 'Jane',
                            'age': 25
                        },
                    ],
                },
            },
            'message': 'Users list',
        }),
        status=200,
        mimetype='application/json'
    )
    return response
