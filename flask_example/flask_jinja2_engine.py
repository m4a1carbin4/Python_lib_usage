from flask import Flask, render_template

app = Flask(__name__)

@app.route('/send')
@app.route('/send/<name>')
def send_html(name=None):
    return render_template('hello.html', name=name) # this will make flask look for templates in ./templates dir => template can use with "Jinja2 template"

#inside template => config,request,session, g, can access as well as url_for(), get_flashed_messages() function.

app.run('localhost',9999,True)