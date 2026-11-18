from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import workplace_service


class WorkplaceController(GeneralController):
    _service = workplace_service

    def get_employees(self, workplace_id: int):
        return self._to_dto_list(self._check_found(self._service.get_employees(workplace_id)))
