from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EquipmentType


class EquipmentTypeDAO(GeneralDAO):
    _domain_type = EquipmentType
