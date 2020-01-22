#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_route():
    return render_template(
        '9-states.html',
        states=storage.all('State').values())


@app.route('/states/<id>')
def statesid_route(id):
    for key, value in storage.all('State').items():
        if value.id == id:
            return render_template('9-states.html', states_id=value)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
