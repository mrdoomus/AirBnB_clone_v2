#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

app.route('/')


@app.route("/", strict_slashes=False)
def print():
    """Return a string"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
