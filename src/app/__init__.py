# app/__init__.py
from flask import Flask
from .database.connection import db_connection

def create_app():
    app = Flask(__name__)

    # Initialize the database connection
    app.db = db_connection()
    if app.db is None:
        raise Exception("Could not connect to the database")

    # Import and register blueprints here if using app factory pattern
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
