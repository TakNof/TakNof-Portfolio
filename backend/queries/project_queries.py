# backend/queries/project_queries.py
from models.projects import Projects
from models.categories import Categories
from models.project_details import ProjectDetails
from flask_restx import abort
from werkzeug.exceptions import HTTPException

class ProjectsQueries:
    @staticmethod
    def get_all_projects():
        """Returns all projects from the database"""
        return Projects.query.all()

    # @staticmethod
    # def get_projects_by_category(category_name):
    #     """Returns all projects from the database"""
    #     return Projects.query.filter(Projects.category.has(name=category_name)).all()

    @staticmethod
    def get_project_by_id(project_id):
        """Returns a specific project or None"""
        return Projects.query.get(project_id)

    @staticmethod
    def get_project_details(project_id):
        """Returns the ordered project_details rows for a project."""
        return (
            ProjectDetails.query
            .filter(ProjectDetails.id_project == project_id)
            .order_by(ProjectDetails.order)
            .all()
        )

    @staticmethod
    def get_projects_by_ids(ids):
        """Returns the projects matching `ids`, in the same order as `ids`."""
        if not ids:
            return []
        rows = Projects.query.filter(Projects.id.in_(ids)).all()
        by_id = {project.id: project for project in rows}
        return [by_id[i] for i in ids if i in by_id]
        
    @staticmethod
    def get_projects_by_category(category_name):
        """Filters projects by category name"""

        category_exists = Categories.query.filter_by(name=category_name).first()
        if not category_exists:
            abort(404, "The category name does not exist in the system")

        rows = (
            Projects.query
            .join(Categories)
            .filter(Categories.name == category_name)
            .all()
        )

        return rows