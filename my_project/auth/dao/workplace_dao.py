from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Workplace


class WorkplaceDAO(GeneralDAO):
    _domain_type = Workplace

    def find_by_office(self, office_id: int):
        return self._session.query(Workplace).filter(Workplace.office_id == office_id).all()
