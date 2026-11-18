from my_project.auth.dao import office_dao, workplace_dao, equipment_dao
from my_project.auth.service.general_service import GeneralService


class OfficeService(GeneralService):
    _dao = office_dao

    def find_by_city(self, city: str):
        return self._dao.find_by_city(city)

    def get_workplaces(self, office_id: int):
        if self.find_by_id(office_id) is None:
            return None
        return workplace_dao.find_by_office(office_id)

    def get_equipment(self, office_id: int, status: str = None):
        if self.find_by_id(office_id) is None:
            return None
        return equipment_dao.find_by_office(office_id, status)
