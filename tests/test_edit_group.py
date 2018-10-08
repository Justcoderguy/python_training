from models.group import Group
__author__ = 'pzqa'


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first(Group(name="Foes", logo="", comment="Stay away!"))
