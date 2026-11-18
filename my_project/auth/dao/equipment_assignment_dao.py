from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import EquipmentAssignment


class EquipmentAssignmentDAO(GeneralDAO):
    _domain_type = EquipmentAssignment
