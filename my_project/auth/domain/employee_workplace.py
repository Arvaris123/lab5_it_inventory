from my_project import db
from my_project.auth.domain.i_dto import IDto


class EmployeeWorkplace(db.Model, IDto):
    __tablename__ = "employee_workplace"

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), primary_key=True)
    workplace_id = db.Column(db.Integer, db.ForeignKey("workplace.id"), primary_key=True)

    employee = db.relationship("Employee")
    workplace = db.relationship("Workplace")

    def put_into_dto(self):
        return {
            "employee_id": self.employee_id,
            "employee": f"{self.employee.last_name} {self.employee.first_name}" if self.employee else None,
            "workplace_id": self.workplace_id,
            "workplace": self.workplace.code if self.workplace else None,
        }

    @staticmethod
    def create_from_dto(dto):
        return EmployeeWorkplace(
            employee_id=dto.get("employee_id"),
            workplace_id=dto.get("workplace_id"),
        )
