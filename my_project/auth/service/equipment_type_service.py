from my_project.auth.dao import equipment_type_dao
from my_project.auth.service.general_service import GeneralService


class EquipmentTypeService(GeneralService):
    _dao = equipment_type_dao

    def get_models(self, equipment_type_id: int):
        equipment_type = self.find_by_id(equipment_type_id)
        return None if equipment_type is None else equipment_type.models
