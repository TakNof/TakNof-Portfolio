from flask_restx import Namespace, fields

class TechBranchesDto:
    api = Namespace('tech-branches', description='Tech branch operations')

    branch_response = api.model('TechBranchResponse', {
        'id': fields.Integer(description='Branch ID'),
        'name': fields.String(description='Branch name'),
    })
