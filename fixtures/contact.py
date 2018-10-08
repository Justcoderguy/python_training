from selenium.webdriver.support.ui import Select
__author__ = 'pzqa'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # init add contact
        wd.find_element_by_link_text("add new").click()
        # add first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.f_name)
        # add middle name
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.m_name)
        # add second name
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.l_name)
        # add nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.n_name)
        # add title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # add company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # add address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_one)
        # add home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        # add mobile phone
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # add work phone
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        # add fax
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # add first email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_one)
        # add second email
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_two)
        # add third email
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_three)
        # add homepage address
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # select birthday data
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # select anniversary data
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # add second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_two)
        # add second phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_two)
        # add notes
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        self.submit_contact()

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def start_edit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt='Edit']").click()

    def edit(self, contact):
        self.start_edit()
        self.fill_contact_form(contact)
        self.end_edit()

    def end_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        self.fill_contact_field("firstname", contact.f_name)
        self.fill_contact_field("middlename", contact.m_name)
        self.fill_contact_field("lastname", contact.l_name)
        self.fill_contact_field("nickname", contact.n_name)
        self.fill_contact_field("title", contact.title)
        self.fill_contact_field("company", contact.company)
        self.fill_contact_field("address", contact.address_one)
        self.fill_contact_field("home", contact.home)
        self.fill_contact_field("mobile", contact.mobile)
        self.fill_contact_field("work", contact.work)
        self.fill_contact_field("fax", contact.fax)
        self.fill_contact_field("email", contact.email_one)
        self.fill_contact_field("email2", contact.email_two)
        self.fill_contact_field("email3", contact.email_three)
        self.fill_contact_field("homepage", contact.homepage)
        self.fill_contact_field("bday", contact.bday)
        self.fill_contact_field("bmonth", contact.bmonth)
        self.fill_contact_field("byear", contact.byear)
        self.fill_contact_field("aday", contact.aday)
        self.fill_contact_field("amonth", contact.amonth)
        self.fill_contact_field("ayear", contact.ayear)
        self.fill_contact_field("address2", contact.address_two)
        self.fill_contact_field("phone2", contact.phone_two)
        self.fill_contact_field("notes", contact.notes)

    def fill_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        self.select_first_contact()
        self.start_edit()
        self.fill_contact_form(contact)
        self.end_edit()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
