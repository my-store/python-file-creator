import mysql.connector as mysql

class Connection :
    def __init__(self) :
        self.db         = mysql.connect(
            host        = "localhost",
            user        = "root",
            password    = "rombax212",
            database    = "rombax_login"
        )
        self.crsr()

    def crsr(self) :
        self.result = self.db.cursor()

    def exc(self, p) :
        self.result.execute(p)

p1 = Connection()

p1.exc("SHOW TABLES")

for x in p1.result :
    print(x)
