from extensions import db

# Many-to-many: a tech belongs to one or more branches (Programming, Web Development, ...)
tech_branch = db.Table('tech_branch',
    db.Column('id_tech', db.Integer, db.ForeignKey('techs.id_tech'), primary_key=True),
    db.Column('id_tech_branch', db.Integer, db.ForeignKey('tech_branches.id_tech_branch'), primary_key=True)
)

class Techs(db.Model):
    id = db.Column('id_tech', db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    rate = db.Column(db.Integer)

    branches = db.relationship(
        'TechBranches',
        secondary=tech_branch,
        lazy='subquery',
        backref=db.backref('techs', lazy=True)
    )
