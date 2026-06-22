from flask_restx import Namespace, fields

class TagsDto:
    api = Namespace('tags', description='Tags operations')

    tag_response = api.model('TagResponse', {
        'id': fields.Integer(description='Tag ID'),
        'name': fields.String(description='Tag name')
    })