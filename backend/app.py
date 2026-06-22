# backend/app.py
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from extensions import db, api
from controllers.project_controller import projectsDto as project_ns

def create_app():
    flask_env = os.getenv('FLASK_ENV', 'development')
    
    if flask_env == 'production':
        load_dotenv('.env.production')
    else:
        load_dotenv('.env.development')

    app = Flask(__name__)
    
    frontend_url = os.getenv('FRONTEND_URL')
    
    CORS(app, origins=[frontend_url])
    
    basedir = os.path.abspath(os.path.dirname(__name__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)
    api.add_namespace(project_ns)
    import models 

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)