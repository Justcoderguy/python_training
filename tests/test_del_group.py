from models.group import Group
__author__ = 'pzqa'


def test_method_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
