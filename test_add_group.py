# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application
__author__ = 'pzqa'


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_method_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Group name", logo="Group logo", comment="Group comment"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", logo="", comment=""))
    app.logout()
