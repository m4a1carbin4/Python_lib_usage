from flask import Flask,request,make_response,redirect,url_for,abort
app = Flask(__name__)

#use cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    
    return f"{username}"
    
#Storing cookies
@app.route('/cookie')
def cookies():
    resp = make_response("hello")
    resp.set_cookie('username','username set')
    return resp

@app.route('/help')
def help_cookie():
    return "host/cookies"

#redirect to help_cookie func ('/help')
@app.route('/getcookie',methods=["POST","GET"])
def getcookie():
    if request.method == "GET":
        return redirect(url_for('help_cookie'))
    else:
        abort(401)
        #never run below
        
@app.errorhandler(401)
def error_401(error):
    return "returned 401 error", 401 # this 401 tell flask that the status code of this page should be 401 (default 200)
        
app.run('localhost',9999,True)

