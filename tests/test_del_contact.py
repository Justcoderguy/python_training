__author__ = 'pzqa'


def test_method_del_contact(app):
    app.contact.delete_first()
