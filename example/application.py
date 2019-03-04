from flask import Flask, jsonify
from example import conn
from example.todo import Todo
from example.configuration import get_config
import example.profile


app = Flask(__name__)
app.config.from_object(get_config())
app.app_context().push()
conn.init_app(app)
profile = example.profile.init()


@app.route('/todos', methods=['GET'])
def get_all():
    rows = Todo.query.all()
    result = []
    # Can't serialize most objects as JSON.
    # (1) First covert each object to a dictionary
    # (2) And add each to a new list.
    for row in rows:
        result.append(row.to_dict())
    return jsonify(todos=result)    # jsonify needs a root in order work with lists


@app.route('/todo/<id>', methods=['GET'])
def get(id):
    row = Todo.query.filter(Todo.id == id).first()
    return jsonify(todo=row.to_dict())


if __name__ == '__main__':
    app.run()
