from my_project import db
from my_project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    position = db.Column(db.String(60), nullable=False)

    workplaces = db.relationship("Workplace", secondary="employee_workplace",
                                 back_populates="employees", viewonly=True)
    assignments = db.relationship("EquipmentAssignment", back_populates="employee", passive_deletes="all")

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "position": self.position,
        }

    @staticmethod
    def create_from_dto(dto):
        return Employee(
            first_name=dto.get("first_name"),
            last_name=dto.get("last_name"),
            email=dto.get("email"),
            position=dto.get("position"),
        )
