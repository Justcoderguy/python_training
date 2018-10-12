from models.contact import Contact
__author__ = 'pzqa'


def test_method_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="Peter"))
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
