from flask_restx import Namespace, fields
from .tech_branches_dto import TechBranchesDto

class TechsDto:
    api = Namespace('techs', description='Techs operations')

    # Lightweight tech shape embedded inside project responses.
    tech_response = api.model('TechResponse', {
        'id': fields.Integer(description='Tech ID'),
        'name': fields.String(description='Tech name'),
        'rate': fields.Integer(description='Proficiency rate (0-10)'),
    })

    # Minimal project reference embedded inside a tech detail.
    tech_project_ref = api.model('TechProjectRef', {
        'id': fields.Integer(description='Project ID'),
        'title': fields.String(description='Project title'),
    })

    # Full tech shape returned by the /techs/ endpoint.
    tech_detail_response = api.inherit('TechDetail', tech_response, {
        'branches': fields.List(fields.Nested(TechBranchesDto.branch_response)),
        'projects': fields.List(fields.Nested(tech_project_ref)),
    })
