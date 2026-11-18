from sqlalchemy import text

from my_project import db


class ProcedureDAO:
    def insert_manufacturer(self, name, country):
        db.session.execute(text("CALL insert_manufacturer(:name, :country)"),
                           {"name": name, "country": country})
        db.session.commit()

    def add_employee_workplace(self, last_name, first_name, code):
        db.session.execute(text("CALL add_employee_workplace(:last_name, :first_name, :code)"),
                           {"last_name": last_name, "first_name": first_name, "code": code})
        db.session.commit()

    def insert_noname_types(self):
        db.session.execute(text("CALL insert_noname_types()"))
        db.session.commit()

    def show_avg_ram(self):
        return db.session.execute(text("CALL show_avg_ram()")).scalar()

    def split_office(self):
        db.session.execute(text("CALL split_office()"))
        db.session.commit()
