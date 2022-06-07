from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app
from config import Config


config = Config()

app.config["SQLALCHEMY_DATABASE_URI"] = config.get_db_uri()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()
