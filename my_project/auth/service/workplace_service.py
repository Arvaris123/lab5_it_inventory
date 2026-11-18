from my_project.auth.dao import workplace_dao
from my_project.auth.service.general_service import GeneralService


class WorkplaceService(GeneralService):
    _dao = workplace_dao

    def get_employees(self, workplace_id: int):
        workplace = self.find_by_id(workplace_id)
        return None if workplace is None else workplace.employees
