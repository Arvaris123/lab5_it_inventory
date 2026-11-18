from my_project.auth.dao import employee_workplace_dao
from my_project.auth.service.general_service import GeneralService


class EmployeeWorkplaceService(GeneralService):
    _dao = employee_workplace_dao
