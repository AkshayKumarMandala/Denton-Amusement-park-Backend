from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configurations from Config class
    db.init_app(app)

    # Additional setup...
    
    return app
