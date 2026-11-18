from my_project import db
from my_project.auth.domain.i_dto import IDto


class Workplace(db.Model, IDto):
    __tablename__ = "workplace"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    office_id = db.Column(db.Integer, db.ForeignKey("office.id"), nullable=False)

    office = db.relationship("Office", back_populates="workplaces")
    employees = db.relationship("Employee", secondary="employee_workplace",
                                back_populates="workplaces", viewonly=True)

    def put_into_dto(self):
        return {
            "id": self.id,
            "code": self.code,
            "room_number": self.room_number,
            "office_id": self.office_id,
            "office": self.office.name if self.office else None,
        }

    @staticmethod
    def create_from_dto(dto):
        return Workplace(
            code=dto.get("code"),
            room_number=dto.get("room_number"),
            office_id=dto.get("office_id"),
        )
