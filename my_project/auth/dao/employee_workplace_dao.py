from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EmployeeWorkplace


class EmployeeWorkplaceDAO(GeneralDAO):
    _domain_type = EmployeeWorkplace

    def update(self, key, new_obj):
        obj = self.find_by_id(key)
        if obj is None:
            return None
        obj.employee_id = new_obj.employee_id
        obj.workplace_id = new_obj.workplace_id
        self._session.commit()
        return obj
