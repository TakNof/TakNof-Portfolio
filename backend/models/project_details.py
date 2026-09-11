from extensions import db
from sqlalchemy import Column, Integer, CHAR, String, ForeignKey, CheckConstraint, Text

class ProjectDetails(db.Model):
    id = Column('id_project_detail', Integer, primary_key=True)
    id_project = Column(Integer, ForeignKey('projects.id_project'), nullable=False)

    title = Column(String(30), nullable=True)
    order = Column(Integer, nullable=False)          # display order within the project
    resource_url = Column(String(255), nullable=True)
    resource_type = Column(CHAR(5), nullable=True)   # e.g. 'image', 'video', 'link'

    info = Column(Text, nullable=False)

    __table_args__ = (
        # resource_type may be NULL only when resource_url is absent (NULL or blank);
        # once a URL is provided, its type must be provided too.
        CheckConstraint(
            "resource_url IS NULL OR resource_url = '' OR resource_type IS NOT NULL",
            name="ck_project_details_type_required_with_url",
        ),
    )