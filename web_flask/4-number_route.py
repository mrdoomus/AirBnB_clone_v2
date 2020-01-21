#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def greet():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python')
def py_route(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>')
def num_route(n):
    return '{:d} is a number'.format(int(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
