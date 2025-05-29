import mysql.connector as m
mydb = m.connect(
  host="localhost",
  user="root",
  password="swordsaint"
)
cur = mydb.cursor()
cur.execute("create database testdb")
cur.execute("use testdb")
cur.execute("create table testtable (id int, name varchar(255))") 
cur.execute("insert into testtable (id, name) values (1, 'test')")
cur.execute("select * from testtable")
for row in cur.fetchall():
    print(row)
mydb.commit()
#test comment