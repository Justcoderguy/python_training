# -*- coding: utf-8 -*-
from models.group import Group
__author__ = 'pzqa'


def test_method_add_group(app):
    app.group.create(Group(name="Group name", logo="Group logo", comment="Group comment"))


def test_add_empty_group(app):
    app.group.create(Group(name="", logo="", comment=""))
