import re
from random import randrange
__author__ = 'pzqa'


def test_data_on_home_page_correspond_edit_page(app):
    app.contact.open_home_page()
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.f_name == contact_from_edit_page.f_name
    assert contact_from_home_page.l_name == contact_from_edit_page.l_name
    assert contact_from_home_page.address_one == contact_from_edit_page.address_one
    assert contact_from_home_page.all_home_page_phones == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_home_page_emails == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone_two == contact_from_edit_page.phone_two


def phone_reg_ex(phone):
    return re.sub('[() -]', '', phone)


def email_reg_ex(email):
    return re.search('.+@.+\..+', email).group()


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: phone_reg_ex(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone_two]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: email_reg_ex(x),
                                filter(lambda x: x is not None,
                                       [contact.email_one, contact.email_two, contact.email_three]))))
