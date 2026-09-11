from extensions import db

class Skills(db.Model):
    id = db.Column('id_skill', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)