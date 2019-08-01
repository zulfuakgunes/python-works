from mysql.connector import connect


class MySQLConnect:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def __enter__(self):
        self.connect = connect(host=self.host, user=self.user, passwd=self.password)
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.close()
