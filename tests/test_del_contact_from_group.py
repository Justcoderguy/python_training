from models.group import Group
from models.contact import Contact
from random import randrange
_author_ = 'pzqa'


def test_del_contact_from_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact())
    if len(db.get_group_list()) == 0:
        app.group.create(Group())
    group_list = db.get_group_list()
    group_index = randrange(len(group_list))
    group_id = group_list[group_index].id
    if len(db.get_contact_group(group_id)) == 0:
        old_contact_group = db.get_contact_group_list()
        contact_index = randrange(len(old_contact_group))
        contact_id = old_contact_group[contact_index].id
        app.contact.add_contact_to_group_by_id(contact_id, group_id)
    old_contact_group = db.get_contact_group(group_id)
    contact_index = randrange(len(old_contact_group))
    contact_id = old_contact_group[contact_index].id
    app.contact.del_contact_from_group_by_id(contact_id, group_id)
    old_contact_group.remove(Contact(id=contact_id, group_id=group_id))
    new_contact_group = db.get_contact_group(group_id)
    assert sorted(old_contact_group, key=Contact.id_or_max) == sorted(new_contact_group, key=Contact.id_or_max)
    if check_ui:
        ui_list = app.contact.get_contacts_in_group_ui_list(group_id)
        new_contact_group = db.get_contact_group(group_id)
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(new_contact_group, key=Contact.id_or_max)


