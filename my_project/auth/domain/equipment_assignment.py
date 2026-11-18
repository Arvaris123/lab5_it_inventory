from datetime import date

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EquipmentAssignment(db.Model, IDto):
    __tablename__ = "equipment_assignment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issued_at = db.Column(db.Date, nullable=False)
    returned_at = db.Column(db.Date, nullable=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=True)
    workplace_id = db.Column(db.Integer, db.ForeignKey("workplace.id"), nullable=True)

    equipment = db.relationship("Equipment", back_populates="assignments")
    employee = db.relationship("Employee", back_populates="assignments")
    workplace = db.relationship("Workplace")

    def put_into_dto(self):
        return {
            "id": self.id,
            "issued_at": self.issued_at.isoformat() if self.issued_at else None,
            "returned_at": self.returned_at.isoformat() if self.returned_at else None,
            "equipment_id": self.equipment_id,
            "inventory_number": self.equipment.inventory_number if self.equipment else None,
            "employee_id": self.employee_id,
            "workplace_id": self.workplace_id,
        }

    @staticmethod
    def create_from_dto(dto):
        issued_at = dto.get("issued_at")
        returned_at = dto.get("returned_at")
        return EquipmentAssignment(
            issued_at=date.fromisoformat(issued_at) if issued_at else None,
            returned_at=date.fromisoformat(returned_at) if returned_at else None,
            equipment_id=dto.get("equipment_id"),
            employee_id=dto.get("employee_id"),
            workplace_id=dto.get("workplace_id"),
        )
