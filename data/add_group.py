from models.group import Group
import random
import string
import json
import os.path

__author__ = 'pzqa'

constant = [
    Group(name="name1", logo="logo1", comment="comment1"),
    Group(name="", logo="", comment="")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_group = [Group(name=name, logo=logo, comment=comment)
              for name in ["", random_string("name", 10)]
              for logo in ["", random_string("logo", 15)]
              for comment in ["", random_string("comment", 10)]]