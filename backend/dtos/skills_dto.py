from flask_restx import Namespace, fields

class SkillsDto:
    api = Namespace('skills', description='Skills operations')

    skill_response = api.model('SkillResponse', {
        'id': fields.Integer(description='Skill ID'),
        'name': fields.String(description='Skill name')
    })