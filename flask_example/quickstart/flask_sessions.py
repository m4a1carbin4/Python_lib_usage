from flask import Flask, session, request, redirect,url_for

app = Flask(__name__)

app.secret_key = 'waganawa_meguming' # this is secret keys => should be random as possible.

@app.route('/')
def index():
    if "username" in session:
        return f'username is : {session["username"]}'
    return "user not logined"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.run('localhost',9999,True)