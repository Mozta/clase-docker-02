from flask import Flask
from database import Database

db = Database()
app = Flask(__name__)


@app.route('/')
def hello_docker():
    return 'Hello from Docker =D'


@app.route('/users')
def list_users():
    users = db.list_users()
    return {'users': users}


@app.route('/add_user/<name>')
def add_user(name):
    db.add_user(name)
    return {'message': 'User added'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
