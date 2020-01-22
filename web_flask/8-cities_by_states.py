#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_states_list():
    return render_template(
        '8-cities_by_states.html',
        states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
