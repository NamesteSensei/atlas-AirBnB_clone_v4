#!/usr/bin/python3
""" Flask route to filter places by Amenity """
from flask import Flask, render_template, request, jsonify
from models import storage
from models.place import Place
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/4-hbnb', methods=['GET', 'POST'])
def hbnb_amenities():
    """Displays places with filters by amenities"""
    if request.method == 'POST':
        # Get the list of Amenity IDs from the form submission (checkboxes)
        amenities = request.form.getlist('amenities')
        if amenities:
            # Get the places that match the selected amenities
            places = storage.all(Place).values()
            filtered_places = [place for place in places if all(amenity.id in [a.id for a in place.amenities] for amenity in amenities)]
        else:
            # If no amenities selected, show all places
            filtered_places = storage.all(Place).values()

        return jsonify([place.to_dict() for place in filtered_places])

    # On GET request, render the page
    amenities = storage.all(Amenity).values()
    return render_template('4-hbnb.html', amenities=amenities)


if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5001')
    app.run(host=host, port=port, threaded=True)
