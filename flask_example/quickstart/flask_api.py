from flask import Flask

app = Flask(__name__)

@app.route('/me')
def return_me():
    me = {"name":__name__}
    
    return me

@app.route("/us")
def return_us():
    
    return [a for a in range(10)]

#in Flask dict or list type will automaticaly converted to JSON response.
app.run("localhost",9999,True)