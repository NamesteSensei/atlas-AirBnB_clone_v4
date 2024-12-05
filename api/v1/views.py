from flask import render_template
from api.v1.views import app_views

@app_views.route('/3-hbnb', methods=['GET'])
def three_hbnb():
    """Handles the 3-hbnb route"""
    return render_template('3-hbnb.html')
