__author__ = 'pzqa'


def test_method_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()
