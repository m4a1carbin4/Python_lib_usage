from flask import Flask,url_for,request,render_template

app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
    
        try:
            if request.form['a'] == request.form['b']:
                return "clear"
            else:
                error = 'a and b not same'
        except KeyError: # if key does not exist in form => raise keyError
            error = 'a and b not exist'
    elif request.method == 'GET':
        error = request.args.get('key',"doesn't exist") # if Params 'key' not found => returned "doesn't exist" to error 
            
            
    return render_template('hello.html',error=error)

app.run("localhost",9999,True)