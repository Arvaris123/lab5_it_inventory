from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import employee_service


class EmployeeController(GeneralController):
    _service = employee_service

    def find_by_last_name(self, last_name: str):
        return self._to_dto_list(self._service.find_by_last_name(last_name))

    def get_workplaces(self, employee_id: int):
        return self._to_dto_list(self._check_found(self._service.get_workplaces(employee_id)))

    def get_assignments(self, employee_id: int):
        return self._to_dto_list(self._check_found(self._service.get_assignments(employee_id)))

    def find_all_with_workplaces(self):
        result = []
        for employee in self._service.find_all():
            dto = employee.put_into_dto()
            dto["workplaces"] = self._to_dto_list(employee.workplaces)
            result.append(dto)
        return result
