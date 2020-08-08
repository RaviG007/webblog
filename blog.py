from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('indexhtml.html')
@app.route('/abouthtml')
def hello_hari():
    name="rahon"
    return render_template('abouthtml.html',namehtml=name)
app.run()