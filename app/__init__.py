from flask import Flask
import os

def create_app(test_config=None):

    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Register Blueprints here
    from .routes import parks_bp
    app.register_blueprint(parks_bp)

    return app