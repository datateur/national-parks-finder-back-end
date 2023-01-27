from flask import Flask
import os

def create_app(test_config=None):

    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Register Blueprints here
    from .routes import parks_bp, activities_bp, topics_bp
    app.register_blueprint(parks_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(topics_bp)

    return app