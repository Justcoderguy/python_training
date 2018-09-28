# -*- coding: utf-8 -*-
import pytest
from fixtures.application import Application
from models.contact import Contact
__author__ = 'pzqa'


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.fill_contact_fields(Contact(f_name='John', m_name='Smith', l_name='Doe', n_name='Anonymous',
                                    title='worker', company='Microsoft', address_one='Redwood 11',
                                    home='7777-777-777', mobile='004911234567890', work='5555-555-555',
                                    fax='12315135', email_one='mail@domaim.com',
                                    email_two='mail@domain.com.de', email_three='mail@subdomain.domain.com',
                                    homepage='http:/example.com', bday='1', bmonth='January', byear='1975',
                                    aday='12', amonth='November', ayear='2010',
                                    address_two='Bluewaters 123', phone_two='+1234567890',
                                    notes='Worker of the year.'))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.fill_contact_fields(Contact(f_name='', m_name='', l_name='', n_name='',
                                    title='', company='', address_one='',
                                    home='', mobile='', work='',
                                    fax='', email_one='',
                                    email_two='', email_three='',
                                    homepage='', bday='', bmonth='-', byear='',
                                    aday='', amonth='-', ayear='',
                                    address_two='', phone_two='',
                                    notes=''))
    app.logout()
