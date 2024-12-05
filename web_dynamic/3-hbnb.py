#!/usr/bin/python3
""" 3-hbnb route """

from flask import render_template
from api.v1.views import app_views
from models import storage
from models.place import Place

@app_views.route('/3-hbnb', methods=['GET'])
def show_places():
    """Returns the 3-hbnb page with dynamic content"""
    places = storage.all(Place)
    return render_template('3-hbnb.html', places=places)
