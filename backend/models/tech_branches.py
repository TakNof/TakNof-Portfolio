from extensions import db

class TechBranches(db.Model):
    id = db.Column('id_tech_branch', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)