from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import equipment_service


class EquipmentController(GeneralController):
    _service = equipment_service

    def get_assignments(self, equipment_id: int):
        return self._to_dto_list(self._check_found(self._service.get_assignments(equipment_id)))
