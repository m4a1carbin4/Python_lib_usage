from flask import Flask,request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload',methods=['GET','POST'])
def upload_file():
    try:
    
        if request.method == 'POST':
            f = request.files['file']
            f.save(f"./{secure_filename(f.filename)}")
            return "clear"
        else :
            return "failed"
        
    except :
        return "key error"
        
app.run('localhost',9999,True)