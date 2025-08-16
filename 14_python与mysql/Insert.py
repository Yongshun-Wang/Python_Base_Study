from pymysql import Connection

con = Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1206",
    autocommit = True
)

print(con.get_server_info())

cursor = con.cursor()

con.select_db("world")

#cursor.execute("create table test_pymysql(id int);")
cursor.execute("insert into student values(1,'李白',22)")

con.close()
