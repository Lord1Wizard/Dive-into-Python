import sqlite3

class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        print(self.get_name())
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None

    def get_name(self):
        # print(self.__name__)
        for i, j in globals().items():
            if j is self:
                return i
    def __eq__(self, other):
        return self.__new__(other)


bd == DB('sqlite.db')
# with bd:
#     pass
    # cur.execute("""create table if not exists users(name,age);""")
    # cur.execute("""insert into users values ('Гвидо', 66);""")
