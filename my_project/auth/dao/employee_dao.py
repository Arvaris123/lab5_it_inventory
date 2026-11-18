from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Employee


class EmployeeDAO(GeneralDAO):
    _domain_type = Employee

    def find_by_last_name(self, last_name: str):
        return self._session.query(Employee).filter(Employee.last_name == last_name).all()
