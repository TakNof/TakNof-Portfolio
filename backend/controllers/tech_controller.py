# backend/controllers/tech_controller.py
from flask import request
from flask_restx import Resource
from dtos.techs_dto import TechsDto
from dtos.tech_branches_dto import TechBranchesDto
from queries.tech_queries import TechsQueries

techsDto = TechsDto.api
techBranchesDto = TechBranchesDto.api

@techsDto.route('/')
class TechList(Resource):
    @techsDto.marshal_list_with(TechsDto.tech_detail_response)
    def get(self):
        """List techs, optionally filtered by ?branch=<name>"""
        branch = request.args.get('branch')
        if branch:
            return TechsQueries.get_techs_by_branch(branch)
        return TechsQueries.get_all_techs()


@techBranchesDto.route('/')
class TechBranchList(Resource):
    @techBranchesDto.marshal_list_with(TechBranchesDto.branch_response)
    def get(self):
        """List all tech branches"""
        return TechsQueries.get_all_branches()
