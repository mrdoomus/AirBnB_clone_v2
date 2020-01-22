#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb_route():
    return render_template(
        '100-hbnb.html',
        states=storage.all('State').values(),
        amenities=storage.all('Amenity').values(),
        places=storage.all('Place').values())


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
