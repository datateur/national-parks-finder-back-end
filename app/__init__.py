from flask import Flask
import os

def create_app(test_config=None):

    app = Flask(__name__)
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # if test_config is None:
    #     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    #         "SQLALCHEMY_DATABASE_URI")
    # else:
    #     app.config["TESTING"] = True
    #     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    #         "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.task import Task
    # from app.models.goal import Goal


    # Register Blueprints here
    from .routes import parks_bp
    app.register_blueprint(parks_bp)
    # app.register_blueprint(goals_bp)

    return app