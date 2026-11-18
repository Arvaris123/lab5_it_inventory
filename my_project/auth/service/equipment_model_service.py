from my_project.auth.dao import equipment_model_dao
from my_project.auth.service.general_service import GeneralService


class EquipmentModelService(GeneralService):
    _dao = equipment_model_dao
