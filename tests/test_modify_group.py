from models.group import Group
__author__ = 'pzqa'


def test_method_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New name"))
    app.session.logout()


def test_method_modify_group_logo(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(logo="New logo"))
    app.session.logout()
