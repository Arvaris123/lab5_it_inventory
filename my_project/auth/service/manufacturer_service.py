from my_project.auth.dao import manufacturer_dao
from my_project.auth.service.general_service import GeneralService


class ManufacturerService(GeneralService):
    _dao = manufacturer_dao

    def get_models(self, manufacturer_id: int):
        manufacturer = self.find_by_id(manufacturer_id)
        return None if manufacturer is None else manufacturer.models
