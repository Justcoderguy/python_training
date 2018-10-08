from models.group import Group
__author__ = 'pzqa'


def test_method_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first()
