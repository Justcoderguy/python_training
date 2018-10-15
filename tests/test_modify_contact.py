from models.contact import Contact
from random import randrange
__author__ = 'pzqa'


def test_modify_f_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="Kevin"))
        app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(f_name="Edward", l_name="Smith")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_m_name(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(m_name="Marvin"))
#         app.open_home_page()
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(m_name="Smith"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
