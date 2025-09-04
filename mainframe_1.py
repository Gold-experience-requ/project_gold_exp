import mysql.connector as m
import os
import sys
import functions as fxn
import db

con = db.con
cur = db.cur

cur.execute("""
    CREATE TABLE IF NOT EXISTS user (
        USER_ID int AUTO_INCREMENT PRIMARY KEY,
        USER_NAME VARCHAR(20) NOT NULL,
        USER_PASSWORD VARCHAR(20) NOT NULL,
        USER_EMAIL VARCHAR(50) NOT NULL,
        USER_MOBILE BIGINT NOT NULL,
        ROLE VARCHAR(40) NOT NULL DEFAULT 'player'
    )
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS score (
        USER_ID int NOT NULL,
        GAME_ID varchar(20) NOT NULL,
        SCORE_VALUE INT NOT NULL,
        TIME_STAMP TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (USER_ID) REFERENCES user(USER_ID)
    )
""")
con.commit()

fxn.welcome_screen()
fxn.mainmenu()


# user admin id = admin
# user admin password = admin@arcade
# user admin email = arcadeworld@arcade.com
