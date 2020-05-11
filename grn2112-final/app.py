# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#home page route
@app.route("/")
def hello():
    return render_template("index.html")

#assignments page route
@app.route("/assignments/")
def assignments():
    return "Welcome to the Assignments page!"

#classes page route
@app.route("/classes/")
def classes():
    return "Welcome to the Classes page!"


#start the server
if __name__ == "__main__":
    app.run()