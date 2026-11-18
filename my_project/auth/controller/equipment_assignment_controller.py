from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import equipment_assignment_service


class EquipmentAssignmentController(GeneralController):
    _service = equipment_assignment_service
