from models.contact import Contact
__author__ = 'pzqa'


def test_method_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="Peter"))
        app.open_home_page()
    app.contact.delete_first()
