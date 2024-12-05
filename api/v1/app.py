from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response


app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)

# Enable CORS for API routes
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage session at the end of each request"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    from os import getenv
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
