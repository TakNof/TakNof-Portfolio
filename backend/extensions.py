# backend/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()
api = Api(
    version='1.0', 
    title='Game Dev Portfolio API', 
    description='API for managing my portfolio projects'
)