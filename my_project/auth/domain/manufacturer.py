from my_project import db
from my_project.auth.domain.i_dto import IDto


class Manufacturer(db.Model, IDto):
    __tablename__ = "manufacturer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    country = db.Column(db.String(60), nullable=False)

    models = db.relationship("EquipmentModel", back_populates="manufacturer", passive_deletes="all")

    def put_into_dto(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
        }

    @staticmethod
    def create_from_dto(dto):
        return Manufacturer(
            name=dto.get("name"),
            country=dto.get("country"),
        )
