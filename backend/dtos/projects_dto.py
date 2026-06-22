from flask_restx import Namespace, fields

class ProjectsDto:
    api = Namespace('projects', description='Project operations')

    minimal_project_response = api.model('mpr', {
        'id': fields.Integer,
        'title': fields.String,
        'status': fields.String,
        'category': fields.String,
    })

    basic_project_response = api.inherit('bpr', minimal_project_response, {
        'date': fields.DateTime,
        'shortDesc': fields.String,
        'tech': fields.List(fields.String, attribute=lambda x: [t.name for t in x.tech_tags])
    })

    # This defines the structure of the JSON response
    full_project_response = api.model('Project', {
        'image': fields.String(attribute='image_url', description='Image URL path'),
        'video': fields.String(attribute='video_url', description='Video URL path'),
        'tech': fields.List(fields.String, attribute=lambda x: [t.name for t in x.tech_tags]),
        'info': fields.Raw(description='Detailed JSON info')
    })