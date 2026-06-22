from extensions import db
from sqlalchemy import JSON

project_tag = db.Table('project_tag',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    status = db.Column(db.String(50))
    short_desc = db.Column(db.String(500))
    image_url = db.Column(db.String(255))
    video_url = db.Column(db.String(255))
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    tags = db.relationship('Tag', secondary=project_tag, lazy='subquery', backref=db.backref('projects', lazy=True))
    
    info = db.Column(JSON)