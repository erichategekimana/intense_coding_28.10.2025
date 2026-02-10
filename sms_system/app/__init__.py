from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from .database import db, init_db


migrate = Migrate()


