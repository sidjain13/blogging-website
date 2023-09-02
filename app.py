from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy  

from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

class Todo(db.Model):
    sno=db.column(db.Integer , primary_key = True)
    title=db.column(db.String(200) , nullable = False)
    desc=db.column(db.String(200) , nullable = False)

    date_created=db.column(db.DateTime , default = datetime.utcnow)

    def __repr__(self) -> str : 
        return f"{self.sno} - {self.title}"
    
    



# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route("/")
def hello_world():
    return render_template ('index.html')

@app.route("/products")
def product():
    return "this is siddhant jain website"

if __name__ == "__main__":
    app.run(debug=True)