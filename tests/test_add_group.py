# -*- coding: utf-8 -*-
from models.group import Group
__author__ = 'pzqa'


def test_method_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group name", logo="Group logo", comment="Group comment"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", logo="", comment=""))
    app.session.logout()
