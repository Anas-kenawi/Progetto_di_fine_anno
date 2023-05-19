from flask import Flask
from flask import render_template
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

app = Flask(__name__)


@app.route("/")
def player_list():
      mycursor.execute("SELECT * FROM INAZUMA_ELEVEN.players")
      myresult = mycursor.fetchall()
      return render_template('site.html', players=myresult)

@app.route("/Mark_Evans")
def Mark_Evans():
      mycursor.execute("SELECT * FROM INAZUMA_ELEVEN.players")
      myresult = mycursor.fetchall()
      return render_template('Mark.html', players=myresult)

