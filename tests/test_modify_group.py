from models.group import Group
__author__ = 'pzqa'


def test_method_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name"))


def test_method_modify_group_logo(app):
    app.group.modify_first_group(Group(logo="New logo"))
