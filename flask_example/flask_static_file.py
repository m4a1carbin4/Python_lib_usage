from flask import Flask,url_for

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_chamcahm():
    return "testing"

with app.app_context(), app.test_request_context():
    url_for('static',filename='chamcham.png')

app.run('localhost',9999,True)