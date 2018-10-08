from models.group import Group
__author__ = 'pzqa'


def test_method_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New name"))


def test_method_modify_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(logo="New logo"))
