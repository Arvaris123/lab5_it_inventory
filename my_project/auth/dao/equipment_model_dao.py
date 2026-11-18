from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EquipmentModel


class EquipmentModelDAO(GeneralDAO):
    _domain_type = EquipmentModel
