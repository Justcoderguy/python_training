import pymysql
from models.group import Group
_author_ = 'pzqa'


class DbFixture:
    def __init__(self, host, name, admin, password):
        self.host = host
        self.name = name
        self.admin = admin
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=admin, password=password, autocommit=True)

    def get_group_list(self):
        l = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer "
                           "FROM group_list")
            for row in cursor:
                (id, name, logo, comment) = row
                l.append(Group(id=str(id), name=name, logo=logo, comment=comment))
        finally:
            cursor.close()
        return l

    def destroy(self):
        self.connection.close()
