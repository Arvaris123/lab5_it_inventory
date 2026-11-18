from my_project import db
from my_project.auth.domain.i_dto import IDto


class ComputerConfiguration(db.Model, IDto):
    __tablename__ = "computer_configuration"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpu = db.Column(db.String(60), nullable=False)
    ram_gb = db.Column(db.Integer, nullable=False)
    storage_gb = db.Column(db.Integer, nullable=False)
    os = db.Column(db.String(40), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "cpu": self.cpu,
            "ram_gb": self.ram_gb,
            "storage_gb": self.storage_gb,
            "os": self.os,
        }

    @staticmethod
    def create_from_dto(dto):
        return ComputerConfiguration(
            cpu=dto.get("cpu"),
            ram_gb=dto.get("ram_gb"),
            storage_gb=dto.get("storage_gb"),
            os=dto.get("os"),
        )
