from fixtures.orm import ORMFixture
from models.group import Group
_author_ = 'pzqa'

db = ORMFixture(host="127.0.0.1", name="addressbook", admin="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="11"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
