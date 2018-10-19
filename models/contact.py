from sys import maxsize
_author_ = 'pzqa'


class Contact:
    def __init__(self, id=None, f_name=None, m_name=None, l_name=None, n_name=None, title=None, company=None,
                 address_one=None, home=None, mobile=None, work=None, fax=None, email_one=None, email_two=None,
                 email_three=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address_two=None, phone_two=None, notes=None, all_home_page_phones=None):
        self.id = id
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.n_name = n_name
        self.title = title
        self.company = company
        self.address_one = address_one
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email_one = email_one
        self.email_two = email_two
        self.email_three = email_three
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address_two = address_two
        self.phone_two = phone_two
        self.notes = notes
        self.all_home_page_phones = all_home_page_phones

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.f_name, self.l_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.f_name is None or self.f_name == other.f_name) \
               and (self.l_name is None or self.l_name == other.l_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
