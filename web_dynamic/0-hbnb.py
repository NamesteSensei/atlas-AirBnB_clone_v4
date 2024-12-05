#!/usr/bin/python3
"""
Script that starts a Flask web application with routes.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a webpage with all states, cities, and amenities
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('0-hbnb.html', states=states, cities=cities)

@app.teardown_appcontext
def teardown(exception):
    """
    Closes the session at the end of each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
