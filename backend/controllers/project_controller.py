# backend/controllers/project_controller.py
from flask_restx import Resource
from dtos.projects_dto import ProjectsDto
from dtos.categories_dto import CategoriesDto
from queries.project_queries import ProjectQueries
from queries.category_queries import CategoryQueries

# Import the namespace and the model limitation from the DTO
projectsDto = ProjectsDto.api
categoriesDto = CategoriesDto.api

@projectsDto.route('/')
class ProjectList(Resource):
    
    @projectsDto.marshal_list_with(ProjectsDto.basic_project_response)
    def get(self):
        """List all projects"""
        # Call the dedicated queries class
        return ProjectQueries.get_all_projects()

@projectsDto.route('/<int:id>')
@projectsDto.param('id', 'The Project identifier')
@projectsDto.response(404, 'Project not found.')
class ProjectDetail(Resource):
    
    @projectsDto.marshal_with(ProjectsDto.basic_project_response)
    def get(self, id):
        """Get a specific project by ID"""
        project = ProjectQueries.get_project_by_id(id)
        if not project:
            projectsDto.abort(404, "Project not found.")
        return project
    
@categoriesDto.route('/')
class CategoryList(Resource):

    categoriesDto.marshal_list_with(CategoriesDto.category_response)
    def get(self):
        categories = CategoryQueries.get_all_categories()
        return categories