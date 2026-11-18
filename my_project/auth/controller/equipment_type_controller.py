from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import equipment_type_service


class EquipmentTypeController(GeneralController):
    _service = equipment_type_service

    def get_models(self, equipment_type_id: int):
        return self._to_dto_list(self._check_found(self._service.get_models(equipment_type_id)))
