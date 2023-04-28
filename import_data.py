# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS INAZUMA_ELEVEN")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS INAZUMA_ELEVEN.players (
    NAME VARCHAR(30) NOT NULL,
    TEAM VARCHAR(30), 
    POSITION VARCHAR(30),
    ELEMENT VARCHAR(30),
    FP INTEGER,
    TP INTEGER,
    KICK INTEGER,
    BODY INTEGER,
    CONTROL INTEGER,
    GUARD INTEGER,
    SPEED INTEGER,
    STAMINA INTEGER,
    GUTS INTEGER,
    1ST_MOVE VARCHAR(30),
    2ND_MOVE VARCHAR(30),
    3RD_MOVE VARCHAR(30),
    4TH_MOVE VARCHAR(30),
    PRIMARY KEY (NAME)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM INAZUMA_ELEVEN.players")
mydb.commit()

#Read data from a csv file
inazuma = pd.read_csv('./inazuma.csv', index_col=False, delimiter = ',')
inazuma = inazuma.fillna('Null')
print(inazuma.head(20))

#Fill the table
for i,row in inazuma.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO INAZUMA_ELEVEN.players VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM INAZUMA_ELEVEN.players")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)