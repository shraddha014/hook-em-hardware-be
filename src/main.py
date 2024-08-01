from flask import Flask
from flask_cors import CORS
from app.routes import main_routes  # Import your routes or blueprints

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register blueprints or add routes
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)
