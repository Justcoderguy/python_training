# -*- coding: utf-8 -*-
from models.group import Group
import pytest
import random
import string
__author__ = 'pzqa'


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_group = [Group(name=name, logo=logo, comment=comment)
              for name in ["", random_string("name", 10)]
              for logo in ["", random_string("logo", 15)]
              for comment in ["", random_string("comment", 10)]]


@pytest.mark.parametrize("group", test_group, ids=[repr(x) for x in test_group])
def test_method_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
