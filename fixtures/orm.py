from pony.orm import *
from models.group import Group
from models.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from datetime import datetime
_author_ = 'pzqa'


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        logo = Optional(str, column='group_header')
        comment = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id',
                       reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        f_name = Optional(str, column='firstname')
        l_name = Optional(str, column='lastname')
        address_one = Optional(str, column='address')
        email_one = Optional(str, column='email')
        email_two = Optional(str, column='email2')
        email_three = Optional(str, column='email3')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone_two = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id',
                     reverse='contacts', lazy=True)

    def __init__(self, host, name, admin, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=admin, password=password, conv=conv)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, logo=group.logo, comment=group.comment)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), f_name=contact.f_name, l_name=contact.l_name,
                           address_one=contact.address_one, email_one=contact.email_one, email_two=contact.email_two,
                           email_three=contact.email_three, home=contact.home, mobile=contact.mobile,
                           work=contact.work, phone_two=contact.phone_two)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model((select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model((select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model((
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))
