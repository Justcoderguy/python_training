# -*- coding: utf-8 -*-
from models.group import Group
import pytest
from data.add_group import constant as test_group
__author__ = 'pzqa'


@pytest.mark.parametrize("group", test_group, ids=[repr(x) for x in test_group])
def test_method_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
