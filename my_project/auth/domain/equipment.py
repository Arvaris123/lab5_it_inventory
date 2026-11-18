from datetime import date

from my_project import db
from my_project.auth.domain.i_dto import IDto

STATUSES = ("В роботі", "На складі", "В ремонті", "Списано")


class Equipment(db.Model, IDto):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inventory_number = db.Column(db.String(20), nullable=False, unique=True)
    serial_number = db.Column(db.String(40), nullable=False, unique=True)
    status = db.Column(db.Enum(*STATUSES, name="status"), nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    equipment_model_id = db.Column(db.Integer, db.ForeignKey("equipment_model.id"), nullable=False)
    computer_configuration_id = db.Column(db.Integer, db.ForeignKey("computer_configuration.id"), nullable=True)
    office_id = db.Column(db.Integer, db.ForeignKey("office.id"), nullable=False)

    equipment_model = db.relationship("EquipmentModel")
    computer_configuration = db.relationship("ComputerConfiguration")
    office = db.relationship("Office", back_populates="equipment")
    assignments = db.relationship("EquipmentAssignment", back_populates="equipment", passive_deletes="all")

    def put_into_dto(self):
        return {
            "id": self.id,
            "inventory_number": self.inventory_number,
            "serial_number": self.serial_number,
            "status": self.status,
            "purchase_date": self.purchase_date.isoformat() if self.purchase_date else None,
            "equipment_model_id": self.equipment_model_id,
            "equipment_model": self.equipment_model.name if self.equipment_model else None,
            "computer_configuration_id": self.computer_configuration_id,
            "office_id": self.office_id,
            "office": self.office.name if self.office else None,
        }

    @staticmethod
    def create_from_dto(dto):
        purchase_date = dto.get("purchase_date")
        return Equipment(
            inventory_number=dto.get("inventory_number"),
            serial_number=dto.get("serial_number"),
            status=dto.get("status"),
            purchase_date=date.fromisoformat(purchase_date) if purchase_date else None,
            equipment_model_id=dto.get("equipment_model_id"),
            computer_configuration_id=dto.get("computer_configuration_id"),
            office_id=dto.get("office_id"),
        )
