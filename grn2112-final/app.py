

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#home page route
@app.route("/")
def hello():
    return render_template("index.html")

#assignments page route
@app.route("/states/")
def assignments():
    return render_template("states.html")

#classes page route
@app.route("/classes/")
def classes():
    return render_template("classes.html")

#start the server
if __name__ == "__main__":
    app.run()