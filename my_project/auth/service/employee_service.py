from my_project.auth.dao import employee_dao
from my_project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):
    _dao = employee_dao

    def find_by_last_name(self, last_name: str):
        return self._dao.find_by_last_name(last_name)

    def get_workplaces(self, employee_id: int):
        employee = self.find_by_id(employee_id)
        return None if employee is None else employee.workplaces

    def get_assignments(self, employee_id: int):
        employee = self.find_by_id(employee_id)
        return None if employee is None else employee.assignments
