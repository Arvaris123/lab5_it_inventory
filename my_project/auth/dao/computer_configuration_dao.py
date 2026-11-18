from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ComputerConfiguration


class ComputerConfigurationDAO(GeneralDAO):
    _domain_type = ComputerConfiguration
