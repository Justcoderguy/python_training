# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from group_contact import GroupPrimalFields, GroupPhoneFields, GroupWebBdayFields, GroupSecondaryFields


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def primal_data_fields(self, wd, group_contact):
        # init add contact
        wd.find_element_by_link_text("add new").click()
        # add first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group_contact.f_name)
        # add middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group_contact.m_name)
        # add second name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group_contact.l_name)
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group_contact.n_name)
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group_contact.title)
        # add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group_contact.company)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group_contact.address_one)

    def phone_data_fields(self, wd, group_contact):
        # add home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group_contact.home)
        # add mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group_contact.mobile)
        # add work phone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(group_contact.work)
        # add fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(group_contact.fax)

    def web_and_bday_fields(self, wd, group):
        # add first email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.email_one)
        # add second email
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(group.email_two)
        # add third email
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(group.email_three)
        # add homepage address
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(group.homepage)
        # select birthday data
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(group.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(group.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group.byear)
        # select anniversary data
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(group.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(group.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(group.ayear)

    def secondary_fields(self, wd, group):
        # add second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(group.address_two)
        # add second phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(group.phone_two)
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(group.notes)

    def submit_contact(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.primal_data_fields(wd, GroupPrimalFields(f_name='John', m_name='Smith', l_name='Doe', n_name='Anonymous',
                                                      title='worker', company='Microsoft', address_one='Redwood 11'))
        self.phone_data_fields(wd, GroupPhoneFields(home='7777-777-777', mobile='004911234567890',
                                                    work='5555-555-555', fax='12315135'))
        self.web_and_bday_fields(wd, GroupWebBdayFields(email_one='mail@domaim.com', email_two='mail@domain.com.de',
                                                        email_three='mail@subdomain.domain.com',
                                                        homepage='http:/example.com', bday='1', bmonth='January',
                                                        byear='1975', aday='12', amonth='November', ayear='2010'))
        self.secondary_fields(wd, GroupSecondaryFields(address_two='Bluewaters 123', phone_two='+1234567890',
                                                       notes='Worker of the year.'))
        self.submit_contact(wd)
        self.return_to_home_page(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.primal_data_fields(wd, GroupPrimalFields(f_name='', m_name='', l_name='', n_name='',
                                                      title='', company='', address_one=''))
        self.phone_data_fields(wd, GroupPhoneFields(home='', mobile='',
                                                    work='', fax=''))
        self.web_and_bday_fields(wd, GroupWebBdayFields(email_one='', email_two='',
                                                        email_three='',
                                                        homepage='', bday='', bmonth='-',
                                                        byear='', aday='', amonth='-', ayear=''))
        self.secondary_fields(wd, GroupSecondaryFields(address_two='', phone_two='',
                                                       notes=''))
        self.submit_contact(wd)
        self.return_to_home_page(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()