from flask import Flask,url_for,request

app = Flask(__name__)

@app.route('/test1',methods=['GET','POST'])
def test():
    if request.method == 'POST':
        return "post check"
    else :
        return "well it is sure that this isn't post method"
    
#flask provides shortcut for decorating such get(),post()....

@app.get('/get')
def test_get():
    return "get method"

@app.post('/post')
def test_post():
    return "post method"

app.run('localhost',9999,True)