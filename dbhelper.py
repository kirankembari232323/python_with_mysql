import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con = connector.connect(
                                    host='localhost',
                                    port='3306',
                                    user='root',
                                    password='Kiran@23',
                                    database='pythontest')
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(200))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    def insert_user(self, userid, username, phone):
        query = "insert into user(userId,userName,phone) values ({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user inserted into DB")

    def fetch_user(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user id :", row[0])
            print("user name :", row[1])
            print("user phone :", row[2])
            print()

    def delete_user(self, userid):
        query = "delete from user where userId= ({})".format(userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user deleted")

    def update_user(self, userid, username, phone):
        query = "update user set  userName = '{}', phone  = '{}' where userId = {}".format(username, phone, userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user update")


helper = DBhelper()
# helper.insert_user(1453, "Kiran", "899997776")
# helper.insert_user(1454, "Sachin", "899997776")
helper.update_user(1452,"Sachin", "899997776")
helper.fetch_user()
#helper.delete_user(1454)


