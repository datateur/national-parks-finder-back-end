from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['DEBUG'] = True

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "SQLALCHEMY_DATABASE_URI")

    # Import models here
    from app.models.park import Park

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import parks_bp, activities_bp, topics_bp
    app.register_blueprint(parks_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(topics_bp)

    CORS(app)
    return app