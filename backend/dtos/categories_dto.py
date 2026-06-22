from flask_restx import Namespace, fields

class CategoriesDto:
    api = Namespace('categories', description='Category operations')

    category_response = api.model('CategoryResponse', {
        'id': fields.Integer(description='Category ID'),
        'name': fields.String(description='Category name')
    })

    category_post = api.model('CategoryPost', {
        'name': fields.String(required=True, description='Category name')
    })