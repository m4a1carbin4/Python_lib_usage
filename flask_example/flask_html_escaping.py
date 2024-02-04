from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "<p>hello world</p>"

@app.route("/<name>") #if /me = > name == me
def hello(name):
    return f"hello {escape(name)}"

app.run(port=9999,host="localhost")