from my_project import create_app

CONFIG = {
    "mysql": {"user": "test", "password": "test", "host": "localhost", "port": 3306, "database": "it_inventory"},
    "flask": {"debug": False, "port": 5000},
}


def test_all_blueprints_registered():
    app = create_app(CONFIG)
    rules = {rule.rule for rule in app.url_map.iter_rules()}
    for prefix in ["/office", "/workplace", "/employee", "/employee-workplace", "/manufacturer",
                   "/equipment-type", "/equipment-model", "/computer-configuration",
                   "/equipment", "/equipment-assignment"]:
        assert prefix in rules


def test_relation_routes_registered():
    app = create_app(CONFIG)
    rules = {rule.rule for rule in app.url_map.iter_rules()}
    assert "/office/<int:office_id>/workplaces" in rules
    assert "/employee/<int:employee_id>/workplaces" in rules
    assert "/workplace/<int:workplace_id>/employees" in rules
