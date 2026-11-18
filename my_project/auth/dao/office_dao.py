from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Office


class OfficeDAO(GeneralDAO):
    _domain_type = Office

    def find_by_city(self, city: str):
        return self._session.query(Office).filter(Office.city == city).all()
