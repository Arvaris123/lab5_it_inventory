from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Equipment


class EquipmentDAO(GeneralDAO):
    _domain_type = Equipment

    def find_by_office(self, office_id: int, status: str = None):
        query = self._session.query(Equipment).filter(Equipment.office_id == office_id)
        if status:
            query = query.filter(Equipment.status == status)
        return query.all()
