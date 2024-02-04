from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def print_user(username):
    return f"user : {escape(username)}"

@app.route('/item/<int:itemNum>')
def print_item_num(itemNum):
    return f"itemNum : {escape(itemNum)}"

@app.route('/path/<path:path>')
def show_path(path):
    return f"input path : {escape(path)}"

#what if not escape?
@app.route('/path_failed/<path:path>')
def show_path_failed(path):
    return f"input path : {path}" # this can make RPC. 

app.run('localhost',9999,True)