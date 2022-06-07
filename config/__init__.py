from decouple import config


class Config():
    DB = {
        'selected': 'default',
        'list': {},
    }

    def __init__(self, db_name=None):

        if db_name is None:
            db_name = self.DB['selected']

        self.DB['selected'] = db_name
        self.DB['list']['default'] = {
            'driver': config('DATABASE_DEFAULT_DRIVER', default='postgresql', cast=str),
            'host': config('DATABASE_DEFAULT_HOST', default='localhost', cast=str),
            'port': config('DATABASE_DEFAULT_PORT', default=5433, cast=int),
            'user': config('DATABASE_DEFAULT_USER', default='postgres', cast=str),
            'password': config('DATABASE_DEFAULT_PASSWORD', default=123456, cast=int),
            'database': config('DATABASE_DEFAULT_NAME', default='python-flask', cast=str),
        }

    def set_db(self, name):
        self.DB['selected'] = name

    def get_db(self):
        return self.DB['list'][self.DB['selected']]

    def get_db_uri(self):
        return '{driver}://{user}:{password}@{host}:{port}/{database}'.format(
            driver=self.DB['list'][self.DB['selected']]['driver'],
            user=self.DB['list'][self.DB['selected']]['user'],
            password=self.DB['list'][self.DB['selected']]['password'],
            host=self.DB['list'][self.DB['selected']]['host'],
            port=self.DB['list'][self.DB['selected']]['port'],
            database=self.DB['list'][self.DB['selected']]['database'],
        )
