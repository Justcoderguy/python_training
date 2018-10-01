from models.group import Group
__author__ = 'pzqa'


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="Friends", logo="None", comment="Welcome everyone!"))
    app.session.logout()
