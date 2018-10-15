# -*- coding: utf-8 -*-
from models.contact import Contact
__author__ = 'pzqa'


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(f_name='John', m_name='Smith', l_name='Doe', n_name='Anonymous',
                      title='worker', company='Microsoft', address_one='Redwood 11',
                      home='7777-777-777', mobile='004911234567890', work='5555-555-555',
                      fax='12315135', email_one='mail@domaim.com',
                      email_two='mail@domain.com.de', email_three='mail@subdomain.domain.com',
                      homepage='http:/example.com', bday='1', bmonth='January', byear='1975',
                      aday='12', amonth='November', ayear='2010',
                      address_two='Bluewaters 123', phone_two='+1234567890',
                      notes='Worker of the year.')
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.add_new(Contact(f_name='', m_name='', l_name='', n_name='',
#                                 title='', company='', address_one='',
#                                 home='', mobile='', work='',
#                                 fax='', email_one='',
#                                 email_two='', email_three='',
#                                 homepage='', bday='', bmonth='-', byear='',
#                                 aday='', amonth='-', ayear='',
#                                 address_two='', phone_two='',
#                                 notes=''))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
