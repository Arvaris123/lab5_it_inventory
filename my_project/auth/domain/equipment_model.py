from my_project import db
from my_project.auth.domain.i_dto import IDto


class EquipmentModel(db.Model, IDto):
    __tablename__ = "equipment_model"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("manufacturer.id"), nullable=False)
    equipment_type_id = db.Column(db.Integer, db.ForeignKey("equipment_type.id"), nullable=False)

    manufacturer = db.relationship("Manufacturer", back_populates="models")
    equipment_type = db.relationship("EquipmentType", back_populates="models")

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "manufacturer_id": self.manufacturer_id,
            "manufacturer": self.manufacturer.name if self.manufacturer else None,
            "equipment_type_id": self.equipment_type_id,
            "equipment_type": self.equipment_type.name if self.equipment_type else None,
        }

    @staticmethod
    def create_from_dto(dto):
        return EquipmentModel(
            name=dto.get("name"),
            manufacturer_id=dto.get("manufacturer_id"),
            equipment_type_id=dto.get("equipment_type_id"),
        )
