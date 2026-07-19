from flask_restx import Namespace, fields
from .categories_dto import CategoriesDto
from .tags_dto import TagsDto

class ProjectsDto:
    api = Namespace('projects', description='Project operations')

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
        'tags': fields.List(fields.Nested(TagsDto.tag_response))
    })

    full_project_response = api.inherit('FullProject', basic_project_response, {
        'info': fields.Raw(description='Detailed JSON info')
    })