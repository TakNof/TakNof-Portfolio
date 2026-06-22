from flask_restx import Namespace, fields

class TagsDto:
    api = Namespace('tags', description='Project operations')

    tag_response = api.model('tr', {
        'id': fields.Integer,
        'name': fields.String
    })