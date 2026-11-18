from my_project.auth.dao import equipment_dao
from my_project.auth.service.general_service import GeneralService


class EquipmentService(GeneralService):
    _dao = equipment_dao

    def get_assignments(self, equipment_id: int):
        equipment = self.find_by_id(equipment_id)
        return None if equipment is None else equipment.assignments
