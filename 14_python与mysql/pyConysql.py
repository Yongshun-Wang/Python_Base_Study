from pymysql import Connection

con = Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "1206",
)

print(con.get_server_info())

cursor = con.cursor()

con.select_db("world")

#cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from student")

results = cursor.fetchall()

for r in results:
    print(r)

con.close()