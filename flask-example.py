from flask import Flask, request, jsonify
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

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
    return todos[id]


@app.route('/')
def hello_world():
    return 'Hello World!'

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)


if __name__ == '__main__':
    app.run()
