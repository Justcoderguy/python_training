from models.contact import Contact
__author__ = 'pzqa'


def test_modify_f_name(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(f_name="Edward"))
    app.session.logout()


def test_modify_m_name(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(m_name="Joseph"))
    app.session.logout()
