from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import computer_configuration_service


class ComputerConfigurationController(GeneralController):
    _service = computer_configuration_service
