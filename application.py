__author__ = 'Philip Ford'

from flask import Flask, jsonify
from todo import Todo
import profile

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def get_all():
    rows = Todo.query.all()
    result = []
    for row in rows:
        result.append(row.to_dict())
    return jsonify(todos=result)    # jsonify needs a root in order work with lists


@app.route('/todos/<id>', methods=['GET'])
def get(id):
    row = Todo.query.filter(Todo.id == id).first()
    return jsonify(todo=row.to_dict())


if __name__ == '__main__':
    app.run()
