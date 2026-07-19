# backend/app.py
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from extensions import db, api
from controllers.project_controller import projectsDto as project_ns
from controllers.project_controller import categoriesDto as category_ns

def load_ns(*args):
    for arg in args:
        api.add_namespace(arg)
        

def create_app():
    # Load default .env first to populate environment variables
    load_dotenv('.env')
    
    flask_env = os.getenv('FLASK_ENV', 'development')
    
    if flask_env == 'production':
        load_dotenv('.env.production', override=True)

    app = Flask(__name__)
    
    if flask_env == 'development':
        app.config['DEBUG'] = True
        
    frontend_url = os.getenv('FRONTEND_URL')
    
    CORS(app, origins=[frontend_url])
    
    basedir = os.path.abspath(os.path.dirname(__name__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)
    load_ns(project_ns, category_ns)
    import models 

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)