from extensions import db

project_skill = db.Table('project_skill',
    db.Column('id_project', db.Integer, db.ForeignKey('projects.id_project'), primary_key=True),
    db.Column('id_skill', db.Integer, db.ForeignKey('skills.id_skill'), primary_key=True)
)

project_tech = db.Table('project_tech', 
    db.Column('id_project', db.Integer, db.ForeignKey('projects.id_project'), primary_key=True),
    db.Column('id_tech', db.Integer, db.ForeignKey('techs.id_tech'),  primary_key=True)
)

class Projects(db.Model):
    id = db.Column('id_project', db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date)
    status = db.Column(db.String(50))
    short_desc = db.Column(db.String(500))
    image_url = db.Column(db.String(255))
    video_url = db.Column(db.String(255))
    
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id_category'), nullable=False)
    skills = db.relationship('Skills', secondary=project_skill, lazy='subquery', backref=db.backref('projects', lazy=True))
    techs = db.relationship('Techs', secondary=project_tech, lazy='subquery', backref=db.backref('projects', lazy=True))

    # Ordered detail rows shown on the project page (see models/project_details.py)
    details = db.relationship(
        'ProjectDetails',
        backref='project',
        order_by='ProjectDetails.order',
        lazy='subquery',
        cascade='all, delete-orphan',
    )