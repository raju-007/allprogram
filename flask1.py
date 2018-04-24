# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:34:34 2018

@author: rajashekhar
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)