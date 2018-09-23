_author_ = 'pzqa'


class GroupPrimalFields:
    def __init__(self, f_name, m_name, l_name, n_name, title, company, address_one):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.n_name = n_name
        self.title = title
        self.company = company
        self.address_one = address_one


class GroupPhoneFields:
    def __init__(self, home, mobile, work, fax):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax


class GroupWebBdayFields:
    def __init__(self, email_one, email_two, email_three, homepage,
                 bday, bmonth, byear, aday, amonth, ayear):
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


class GroupSecondaryFields:
    def __init__(self, address_two, phone_two, notes):
        self.address_two = address_two
        self.phone_two = phone_two
        self.notes = notes
