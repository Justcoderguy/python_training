from models.contact import Contact
__author__ = 'pzqa'


def test_modify_f_name(app):
    app.contact.modify_first_contact(Contact(f_name="Edward"))


def test_modify_m_name(app):
    app.contact.modify_first_contact(Contact(m_name="Joseph"))
