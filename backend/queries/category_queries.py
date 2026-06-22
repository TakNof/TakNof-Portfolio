# backend/queries/project_queries.py
from models.category import Category

class CategoryQueries:
    @staticmethod
    def get_all_categories():
        """Returns all tags from the database"""
        return Category.query.all()

    @staticmethod
    def get_categories_by_id(id):
        """Returns a specific category or None"""
        return Category.query.get(id)