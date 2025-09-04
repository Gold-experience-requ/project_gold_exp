import mysql.connector as m

con = m.connect(
    host="localhost",
    user="root",
    password="swordsaint",
    database="arcade"
)
cur = con.cursor()
cur.execute("use arcade")