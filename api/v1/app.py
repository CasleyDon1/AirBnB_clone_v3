#!/usr/bin/python3
"""
app.py to connect to API
"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(self):
    """teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    web_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    web_port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=web_host, port=web_port, threaded=True)
