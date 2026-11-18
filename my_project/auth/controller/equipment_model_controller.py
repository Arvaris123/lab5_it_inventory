from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import equipment_model_service


class EquipmentModelController(GeneralController):
    _service = equipment_model_service
