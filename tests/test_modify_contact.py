from models.contact import Contact
__author__ = 'pzqa'


def test_modify_f_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="Kevin"))
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(f_name="Edward"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_m_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(m_name="Marvin"))
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(m_name="Joseph"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
