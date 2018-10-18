import re
from selenium.webdriver.support.ui import Select
from models.contact import Contact
__author__ = 'pzqa'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.submit_contact()
        self.return_to_home_page()
        self.contact_cache = None

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@type='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()

    def start_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()

    def edit(self, index, contact):
        self.start_edit(index)
        self.fill_contact_form(contact)
        self.end_edit()

    def end_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

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
        self.select_contact_option("bday", contact.bday)
        self.select_contact_option("bmonth", contact.bmonth)
        self.fill_contact_field("byear", contact.byear)
        self.select_contact_option("aday", contact.aday)
        self.select_contact_option("amonth", contact.amonth)
        self.fill_contact_field("ayear", contact.ayear)
        self.fill_contact_field("address2", contact.address_two)
        self.fill_contact_field("phone2", contact.phone_two)
        self.fill_contact_field("notes", contact.notes)

    def select_contact_option(self, selector, option):
        wd = self.app.wd
        if option is not None:
            wd.find_element_by_name(selector).click()
            Select(wd.find_element_by_name(selector)).select_by_visible_text(option)
            wd.find_element_by_name(selector).click()

    def fill_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        self.start_edit(index)
        self.fill_contact_form(contact)
        self.end_edit()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                f_text = cells[1].text
                l_text = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(id=id, f_name=f_text, l_name=l_text, home=all_phones[0],
                                                  work=all_phones[2], mobile=all_phones[1], phone_two=all_phones[3]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.start_edit(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_two = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(f_name=firstname, l_name=lastname, id=id, home=home,
                       work=work, mobile=mobile, phone_two=phone_two)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_xpath("//tr[@name='entry']")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone_two = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone_two=phone_two)
