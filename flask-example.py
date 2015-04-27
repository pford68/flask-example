from flask import Flask, request, jsonify

app = Flask(__name__)

todos = {
    '1': "Remember the milk",
    '2': 'Get coffee creamer',
    '3': 'Call Professor Foster',
    '4': 'Check out the TPMS warning in the Audi'
}


@app.route('/todos')
def getAll():
    return jsonify(todos)

@app.route('/todos/<id>')
def get(id):
    return todos.get(id)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
