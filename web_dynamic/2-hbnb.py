#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import uuid

app = Flask(__name__)

@app.route('/2-hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a webpage with all states, cities, and amenities.
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    cache_id = str(uuid.uuid4())  # Add a cache-busting UUID
    return render_template('2-hbnb.html', states=states, cities=cities, amenities=amenities, cache_id=cache_id)

@app.teardown_appcontext
def teardown(exception):
    """
    Closes the session at the end of each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
