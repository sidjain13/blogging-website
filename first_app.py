from flask import Flask 
app = Flask (__name__)
@app.route('/')
def hello():
    return "hello world"

@app.route("/jain")
def world():
    return "siddhant jain "

app.run()