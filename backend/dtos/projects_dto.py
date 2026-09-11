from flask_restx import Namespace, fields
from .categories_dto import CategoriesDto
from .skills_dto import SkillsDto
from .techs_dto import TechsDto

class ProjectsDto:
    api = Namespace('projects', description='Project operations')

    project_detail_response = api.model('ProjectDetailItem', {
        'id': fields.Integer(description='Detail row ID'),
        'order': fields.Integer(description='Display order within the project'),
        'title': fields.String(description='Section title'),
        'info': fields.String(description='Section body text'),
        'url': fields.String(attribute='resource_url', description='Resource URL'),
        'type': fields.String(attribute='resource_type', description='Resource type (image, video, link, ...)'),
    })

    minimal_project_response = api.model('MinimalProject', {
        'id': fields.Integer(description='Project ID'),
        'title': fields.String(description='Project Title'),
        'status': fields.String(description='Project Status'),
        'category': fields.Nested(CategoriesDto.category_response)
    })

    basic_project_response = api.inherit('BasicProject', minimal_project_response, {
        'date': fields.Date(description='Project Date'),
        'shortDesc': fields.String(attribute='short_desc', description='Short description'),
        'image': fields.String(attribute='image_url', description='Image URL path'),
        'video': fields.String(attribute='video_url', description='Video URL path'),
        'skills': fields.List(fields.Nested(SkillsDto.skill_response)),
        'techs': fields.List(fields.Nested(TechsDto.tech_response))
    })

    full_project_response = api.inherit('FullProject', basic_project_response, {
        'details': fields.List(
            fields.Nested(project_detail_response),
            attribute='details',
            description='Ordered detail rows from the project_details table',
        )
    })