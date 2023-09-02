from flask import Flask , render_template

app = Flask(__name__)
@app.route('/')

def hello():
    name="bittu"
    return render_template('index1.html' , name2 = name)

app.run()