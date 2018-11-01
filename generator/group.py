from models.group import Group
import random
import string
import getopt
import sys
import os.path
import json
__author__ = 'pzqa'

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_group = [Group(name="", logo="", comment="")] + [
    Group(name=random_string("name", 10), logo=random_string("logo", 20), comment=random_string("comment", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_group, default=lambda x: x.__dict__, indent=2))

