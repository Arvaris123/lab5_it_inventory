from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import office_service


class OfficeController(GeneralController):
    _service = office_service

    def find_by_city(self, city: str):
        return self._to_dto_list(self._service.find_by_city(city))

    def get_workplaces(self, office_id: int):
        return self._to_dto_list(self._check_found(self._service.get_workplaces(office_id)))

    def get_equipment(self, office_id: int, status: str = None):
        return self._to_dto_list(self._check_found(self._service.get_equipment(office_id, status)))

    def find_all_with_workplaces(self):
        result = []
        for office in self._service.find_all():
            dto = office.put_into_dto()
            dto["workplaces"] = self._to_dto_list(office.workplaces)
            result.append(dto)
        return result
