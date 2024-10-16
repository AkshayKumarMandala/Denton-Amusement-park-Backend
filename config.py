import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Tejesh%402001@localhost:3306/denton_amusement'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'  # Support for CORS headers
    JSONIFY_PRETTYPRINT_REGULAR = True  # Enable pretty print for JSON responses
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
