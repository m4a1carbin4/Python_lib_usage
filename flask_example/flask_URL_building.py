from flask import Flask,url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/login')
def login():
    return "login"

@app.route('/user/<username>')
def profile(username):
    return f'username : {escape(username)}'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='WaGaNaWa'))
    
    #url_for => check current urls for funtion => dont need to remember everything.
    
app.run('localhost',9999,True)