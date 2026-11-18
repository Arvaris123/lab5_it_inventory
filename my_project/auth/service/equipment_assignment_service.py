from my_project.auth.dao import equipment_assignment_dao
from my_project.auth.service.general_service import GeneralService


class EquipmentAssignmentService(GeneralService):
    _dao = equipment_assignment_dao
