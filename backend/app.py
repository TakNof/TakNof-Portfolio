# backend/app.py
from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Allow Cross-Origin Requests from your Vue app

# Setup simple SQLite database
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app, version='1.0', title='Game Dev Portfolio API', description='A simple API for my games')

# 1. Database Model
class GameProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    engine = db.Column(db.String(50), nullable=False) # e.g., Unity, Unreal, Godot
    link = db.Column(db.String(200), nullable=True)

# 2. RestX DTO (Data Transfer Object) for Swagger Serialization
game_model = api.model('Game', {
    'id': fields.Integer(readonly=True, description='The unique identifier'),
    'title': fields.String(required=True, description='Game title'),
    'description': fields.String(required=True, description='Game description'),
    'engine': fields.String(required=True, description='Game engine used'),
    'link': fields.String(description='Link to play/download')
})

# 3. API Namespace and Endpoints
ns = api.namespace('api/games', description='Game operations')

@ns.route('/')
class GameList(Resource):
    @ns.marshal_list_with(game_model)
    def get(self):
        """List all games"""
        games = GameProject.query.all()
        return games

# Initialize DB and run
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Seed initial data if empty
        if not GameProject.query.first():
            demo_game = GameProject(title="Epic RPG", description="A 2D RPG made for a Game Jam.", engine="Godot", link="https://itch.io")
            db.session.add(demo_game)
            db.session.commit()
            
    app.run(debug=True, port=5000)