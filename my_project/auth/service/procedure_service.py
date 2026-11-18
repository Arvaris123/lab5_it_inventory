from my_project.auth.dao import procedure_dao


class ProcedureService:
    _dao = procedure_dao

    def insert_manufacturer(self, name, country):
        self._dao.insert_manufacturer(name, country)

    def add_employee_workplace(self, last_name, first_name, code):
        self._dao.add_employee_workplace(last_name, first_name, code)

    def insert_noname_types(self):
        self._dao.insert_noname_types()

    def show_avg_ram(self):
        return self._dao.show_avg_ram()

    def split_office(self):
        self._dao.split_office()
