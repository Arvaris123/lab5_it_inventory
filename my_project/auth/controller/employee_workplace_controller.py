from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import employee_workplace_service


class EmployeeWorkplaceController(GeneralController):
    _service = employee_workplace_service
