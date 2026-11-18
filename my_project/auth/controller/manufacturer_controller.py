from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import manufacturer_service


class ManufacturerController(GeneralController):
    _service = manufacturer_service

    def get_models(self, manufacturer_id: int):
        return self._to_dto_list(self._check_found(self._service.get_models(manufacturer_id)))
