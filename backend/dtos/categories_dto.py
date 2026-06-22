from flask_restx import Namespace, fields

class CategoriesDto:
    api = Namespace('categories', description='Project operations')

    category_response = api.model('cat_res', {
        'id': fields.Integer,
        'name': fields.String
    })

    category_post = api.model('cat_post', {
        'name': fields.String
    })