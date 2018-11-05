from models.contact import Contact
from random import randrange
__author__ = 'pzqa'


def test_modify_f_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(f_name="Kevin"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(f_name="Edward", l_name="Smith")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
