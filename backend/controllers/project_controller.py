# backend/controllers/project_controller.py
from flask import request
from flask_restx import Resource
from dtos.projects_dto import ProjectsDto
from dtos.categories_dto import CategoriesDto
from queries.project_queries import ProjectsQueries
from queries.category_queries import CategoriesQueries

# Import the namespace and the model limitation from the DTO
projectsDto = ProjectsDto.api
categoriesDto = CategoriesDto.api

@projectsDto.route('/')
class ProjectList(Resource):
    @projectsDto.marshal_list_with(ProjectsDto.basic_project_response)
    def get(self):
        """List all projects"""
        category = request.args.get('category')
        if category:
            # Call the dedicated queries class
            return ProjectsQueries.get_projects_by_category(category)  
        else:
            return ProjectsQueries.get_all_projects()
            

@projectsDto.route('/by-ids')
@projectsDto.param('ids', 'Comma-separated project ids, e.g. 3,5,9')
class ProjectsByIds(Resource):
    @projectsDto.marshal_list_with(ProjectsDto.basic_project_response)
    def get(self):
        """Get several projects at once, ordered to match the requested ids"""
        raw = request.args.get('ids', '')
        ids = []
        for chunk in raw.split(','):
            chunk = chunk.strip()
            if not chunk:
                continue
            try:
                ids.append(int(chunk))
            except ValueError:
                projectsDto.abort(400, f"Invalid project id: '{chunk}'")
        return ProjectsQueries.get_projects_by_ids(ids)


@projectsDto.route('/<int:id>')
@projectsDto.param('id', 'The Project identifier')
@projectsDto.response(404, 'Project not found.')
class ProjectDetail(Resource):

    @projectsDto.marshal_with(ProjectsDto.full_project_response)
    def get(self, id):
        """Get a specific project by ID, including its ordered detail rows"""
        project = ProjectsQueries.get_project_by_id(id)
        if not project:
            projectsDto.abort(404, "Project not found.")
        return project


@projectsDto.route('/<int:id>/details')
@projectsDto.param('id', 'The Project identifier')
@projectsDto.response(404, 'Project not found.')
class ProjectFullInfo(Resource):

    @projectsDto.marshal_list_with(ProjectsDto.project_detail_response)
    def get(self, id):
        """Get the ordered detail rows (full info) for a project"""
        project = ProjectsQueries.get_project_by_id(id)
        if not project:
            projectsDto.abort(404, "Project not found.")
        return ProjectsQueries.get_project_details(id)
    
@categoriesDto.route('/')
class CategoryList(Resource):

    @categoriesDto.marshal_list_with(CategoriesDto.category_response)
    def get(self):
        categories = CategoriesQueries.get_all_categories()
        return categories