from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Manufacturer


class ManufacturerDAO(GeneralDAO):
    _domain_type = Manufacturer
