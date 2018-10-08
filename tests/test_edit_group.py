from models.group import Group
__author__ = 'pzqa'


def test_edit_group(app):
    app.group.edit_first(Group(name="Friends", logo="None", comment="Welcome everyone!"))
