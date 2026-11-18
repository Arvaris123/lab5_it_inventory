from my_project import db
from my_project.auth.domain.i_dto import IDto


class Office(db.Model, IDto):
    __tablename__ = "office"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    city = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(150), nullable=False)

    workplaces = db.relationship("Workplace", back_populates="office", passive_deletes="all")
    equipment = db.relationship("Equipment", back_populates="office", passive_deletes="all")

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "address": self.address,
        }

    @staticmethod
    def create_from_dto(dto):
        return Office(
            name=dto.get("name"),
            city=dto.get("city"),
            address=dto.get("address"),
        )
