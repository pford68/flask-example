from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from configuration import get_config

application = Flask(__name__)
application.config.from_object(get_config())
db = SQLAlchemy(application)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(50), unique=True)
    description = db.Column("description", db.String(255), unique=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Todo(id='%d', name='%s', description='%s')>" % (self.id, self.name, self.description)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
