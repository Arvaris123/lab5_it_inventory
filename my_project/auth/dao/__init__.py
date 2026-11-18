from .office_dao import OfficeDAO
from .workplace_dao import WorkplaceDAO
from .employee_dao import EmployeeDAO
from .employee_workplace_dao import EmployeeWorkplaceDAO
from .manufacturer_dao import ManufacturerDAO
from .equipment_type_dao import EquipmentTypeDAO
from .equipment_model_dao import EquipmentModelDAO
from .computer_configuration_dao import ComputerConfigurationDAO
from .equipment_dao import EquipmentDAO
from .equipment_assignment_dao import EquipmentAssignmentDAO
from .procedure_dao import ProcedureDAO

office_dao = OfficeDAO()
workplace_dao = WorkplaceDAO()
employee_dao = EmployeeDAO()
employee_workplace_dao = EmployeeWorkplaceDAO()
manufacturer_dao = ManufacturerDAO()
equipment_type_dao = EquipmentTypeDAO()
equipment_model_dao = EquipmentModelDAO()
computer_configuration_dao = ComputerConfigurationDAO()
equipment_dao = EquipmentDAO()
equipment_assignment_dao = EquipmentAssignmentDAO()
procedure_dao = ProcedureDAO()
