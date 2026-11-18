from .office_service import OfficeService
from .workplace_service import WorkplaceService
from .employee_service import EmployeeService
from .employee_workplace_service import EmployeeWorkplaceService
from .manufacturer_service import ManufacturerService
from .equipment_type_service import EquipmentTypeService
from .equipment_model_service import EquipmentModelService
from .computer_configuration_service import ComputerConfigurationService
from .equipment_service import EquipmentService
from .equipment_assignment_service import EquipmentAssignmentService
from .procedure_service import ProcedureService

office_service = OfficeService()
workplace_service = WorkplaceService()
employee_service = EmployeeService()
employee_workplace_service = EmployeeWorkplaceService()
manufacturer_service = ManufacturerService()
equipment_type_service = EquipmentTypeService()
equipment_model_service = EquipmentModelService()
computer_configuration_service = ComputerConfigurationService()
equipment_service = EquipmentService()
equipment_assignment_service = EquipmentAssignmentService()
procedure_service = ProcedureService()
