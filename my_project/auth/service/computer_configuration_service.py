from my_project.auth.dao import computer_configuration_dao
from my_project.auth.service.general_service import GeneralService


class ComputerConfigurationService(GeneralService):
    _dao = computer_configuration_dao
