# backend/queries/project_queries.py
from models.project import Project
from models.category import Category

class ProjectQueries:
    @staticmethod
    def get_all_projects():
        """Returns all projects from the database"""
        return Project.query.all()

    @staticmethod
    def get_project_by_id(project_id):
        """Returns a specific project or None"""
        return Project.query.get(project_id)
        
    @staticmethod
    def get_projects_by_category(category_name):
        """Filters projects by category name"""
        return Project.query.join(Category).filter(Category.name == category_name).all()