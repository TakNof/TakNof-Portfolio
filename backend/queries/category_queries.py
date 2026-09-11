# backend/queries/project_queries.py
from models.categories import Categories

class CategoriesQueries:
    @staticmethod
    def get_all_categories():
        """Returns all categories from the database"""
        return Categories.query.all()

    @staticmethod
    def get_categories_by_id(id):
        """Returns a specific category or None"""
        return Categories.query.get(id)
