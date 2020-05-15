# ****************************************************
# Flask Server
# Ganesan Narayanan
# grn2112
# Final          
# ENGI E1006
# Sets up a local Flask server allowing user to traverse
# through a series of webpages. 
# *******************************************************


#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#homepage route
@app.route("/")
def home():
    return render_template("index.html")

#classes page route
@app.route("/classes/")
def classes():
    return render_template("classes.html")

#states page route
@app.route("/states/")
def states():
    return render_template("states.html")

#start the server
if __name__ == "__main__":
    app.run()