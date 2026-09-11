# backend/queries/tech_queries.py
from models.techs import Techs
from models.tech_branches import TechBranches
from flask_restx import abort

class TechsQueries:
    # NULL rates sort last, then highest rate first, then name.
    _order = (Techs.rate.is_(None), Techs.rate.desc(), Techs.name)

    @staticmethod
    def get_all_techs():
        """Returns every tech."""
        return Techs.query.order_by(*TechsQueries._order).all()

    @staticmethod
    def get_techs_by_branch(branch_name):
        """Returns the techs classified under the given branch name."""
        branch = TechBranches.query.filter_by(name=branch_name).first()
        if not branch:
            abort(404, "The tech branch does not exist in the system")

        return (
            Techs.query
            .join(Techs.branches)
            .filter(TechBranches.name == branch_name)
            .order_by(*TechsQueries._order)
            .all()
        )

    @staticmethod
    def get_all_branches():
        """Returns every tech branch."""
        return TechBranches.query.order_by(TechBranches.name).all()
