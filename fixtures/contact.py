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
        self.open_home_page()
        self.contact_cache = None

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@type='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()

    def start_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def start_edit_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_element_by_xpath("//input[@value='%s']/../.." % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def edit(self, index, contact):
        self.start_edit_by_index(index)
        self.fill_contact_form(contact)
        self.end_edit()

    def end_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.open_home_page()

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
        self.start_edit_by_index(index)
        self.fill_contact_form(contact)
        self.end_edit()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        self.start_edit_by_id(id)
        self.fill_contact_form(contact)
        self.end_edit()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            self.open_home_page()
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("id")
                f_text = cells[2].text
                l_text = cells[1].text
                address_text = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, f_name=f_text, l_name=l_text, address_one=address_text,
                                                  all_home_page_emails=all_emails, all_home_page_phones=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.start_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address_one = wd.find_element_by_name("address").text
        email_one = wd.find_element_by_name("email").get_attribute("value")
        email_two = wd.find_element_by_name("email2").get_attribute("value")
        email_three = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone_two = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, f_name=firstname, l_name=lastname, address_one=address_one,
                       email_one=email_one, email_two=email_two, email_three=email_three,
                       home=home, mobile=mobile, work=work, phone_two=phone_two)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        row = wd.find_elements_by_name("entry")[index]
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

    def add_contact_to_group_by_id(self, contact_id, group_id):
        self.open_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_to_add_to(group_id)

    def select_group_to_add_to(self, group_id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']").click()
        Select(wd.find_element_by_xpath("//select[@name='to_group']")).select_by_value(group_id)
        wd.find_element_by_xpath("//input[@name='add']").click()
        wd.find_element_by_xpath("//a[contains(text(), 'group page')]").click()

    def get_contacts_in_group_ui_list(self, group_id):
        wd = self.app.wd
        self.open_contacts_in_group(group_id)
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("id")
            self.contact_cache.append(Contact(id=id))
        return list(self.contact_cache)

    def open_contacts_in_group(self, group_id):
        wd = self.app.wd
        if self.contact_cache is None:
            self.contact_cache = []
        if wd.current_url != ("http://localhost/addressbook/?group=%s" % group_id):
            wd.get("http://localhost/addressbook/?group=%s" % group_id)

    def del_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_in_group(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//input[@name='remove']").click()
        wd.find_element_by_xpath("//a[contains(text(), 'group page')]").click()

