#!/usr/bin/python3
"""Shebang"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    t = text.replace("_", " ")
    return "C " + t


@app.route('/python/<text>', strict_slashes=False)
def py(text):
    txt = text.replace('_', ' ')
    return f"Python {txt}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
