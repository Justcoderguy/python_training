from models.contact import Contact
__author__ = 'pzqa'


def test_modify_f_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(f_name="Kevin"))
        app.open_home_page()
    app.contact.modify_first_contact(Contact(f_name="Edward"))


def test_modify_m_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(m_name="Marvin"))
        app.open_home_page()
    app.contact.modify_first_contact(Contact(m_name="Joseph"))
