# -*- coding: utf-8 -*-
from models.group import Group
__author__ = 'pzqa'


def test_method_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Group name", logo="Group logo", comment="Group comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", logo="", comment=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
