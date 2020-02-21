class Student:

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return repr(f"{self.first}, {self.last}, {self.email}")


class Connect:

    def __init__(self, file):
        self.file = file

    def __enter__(self):
        import sqlite3
        try:
            self.connect = sqlite3.connect(self.file)
        except Exception:
            raise ValueError("Connection problem")
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()


with Connect('my.db') as con:
    try:
        connect = con.cursor()
        connect.execute("""CREATE TABLE thestudents(
        fullname text,
        email TEXT NOT NULL UNIQUE
        )""")
        con.commit()
    except Exception:
        pass


with Connect('my.db') as c:
    h = Student("Halil", "Yıldırım", "halil@halil.site")
    cn = c.cursor()
    cn.execute(f"INSERT INTO thestudents VALUES ('{h.fullname}', '{h.email}')")
    c.commit()
    cn.execute("SELECT * FROM thestudents WHERE email='halil@halil.site'")
    print(cn.fetchone())
