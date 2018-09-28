__author__ = 'pzqa'


def test_method_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()
