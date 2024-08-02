from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints here if using app factory pattern
    from .routes import main_routes
    app.register_blueprint(main_routes)

    return app
