# -*- coding: utf-8 -*-
from models.contact import Contact
import random
import string
import pytest
__author__ = 'pzqa'


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_contact = [Contact(f_name=f_name, m_name=m_name, l_name=l_name, n_name=n_name,
                        title=title, company=company, address_one=address_one,
                        home='7777777777', mobile='4912331321', work='456321345613',
                        fax='5544341233', email_one='mail@domain.com',
                        email_two='someser@somedomain.de', email_three='anyuser@anydomain.net',
                        homepage='www.example.com', bday='1', bmonth='January', byear='1975',
                        aday='12', amonth='November', ayear='2010',
                        address_two=address_two, phone_two='4426313451235',
                        notes=notes)
                for f_name in ["", random_string("f_name", 10)]
                for m_name in ["", random_string("m_name", 10)]
                for l_name in ["", random_string("l_name", 10)]
                for n_name in ["", random_string("n_name", 10)]
                for title in ["", random_string("title", 10)]
                for company in ["", random_string("company", 10)]
                for address_one in ["", random_string("address_one", 10)]
                for notes in ["", random_string("notes", 10)]
                for address_two in ["", random_string("address_two", 10)]
                ]


@pytest.mark.parametrize("contact", test_contact, ids=[repr(x) for x in test_contact])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
