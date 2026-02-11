from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from .database import db, init_db


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    init_db(app)
    migrate.init_app(app, db)

    # Enabling CORS
    CORS(app, resouces={r"/api/*": {"origins": "*"}})
