from extensions import db

class Categories(db.Model):
    id = db.Column('id_category', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    projects = db.relationship('Projects', backref='category', lazy=True)