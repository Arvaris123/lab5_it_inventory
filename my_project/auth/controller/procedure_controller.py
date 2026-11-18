from my_project.auth.service import procedure_service


class ProcedureController:
    _service = procedure_service

    def insert_manufacturer(self, name, country):
        self._service.insert_manufacturer(name, country)

    def add_employee_workplace(self, last_name, first_name, code):
        self._service.add_employee_workplace(last_name, first_name, code)

    def insert_noname_types(self):
        self._service.insert_noname_types()

    def show_avg_ram(self):
        return self._service.show_avg_ram()

    def split_office(self):
        self._service.split_office()
