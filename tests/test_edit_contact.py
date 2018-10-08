from models.contact import Contact
__author__ = 'pzqa'


def test_edit_contact(app):
    app.contact.edit(Contact(f_name='Janna', m_name='Johanna', l_name='Johnson', n_name='nonickname',
                             title='student', company='Apple', address_one='Greenfields 15-A',
                             home='9999-888-666', mobile='+4943587901234', work='1111-111-111',
                             fax='75799753', email_one='user@somedomain.org',
                             email_two='user@somedomain.net', email_three='user@subdomain.domain.com.de',
                             homepage='http:/example.com.de', bday='5', bmonth='June', byear='1996',
                             aday='3', amonth='February', ayear='2005',
                             address_two='Blackwoods 675', phone_two='3123523123',
                             notes='Nubie.'))
