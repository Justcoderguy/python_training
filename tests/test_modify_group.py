from models.group import Group
__author__ = 'pzqa'


def test_method_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_method_modify_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(logo="New logo"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
