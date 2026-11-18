from my_project import db
from my_project.auth.domain.i_dto import IDto


class EquipmentType(db.Model, IDto):
    __tablename__ = "equipment_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False, unique=True)

    models = db.relationship("EquipmentModel", back_populates="equipment_type", passive_deletes="all")

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto):
        return EquipmentType(name=dto.get("name"))
