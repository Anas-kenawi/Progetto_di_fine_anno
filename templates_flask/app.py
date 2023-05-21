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

@app.route("/Mark")
def portiere():      
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Mark Evans'")
      statistiche = mycursor.fetchall()
      return render_template('Mark.html', statistiche=statistiche)

@app.route("/Axel")
def attaccante_1():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Axel Blaze'")
      statistiche_1 = mycursor.fetchall()
      return render_template('Axel.html', statistiche_1=statistiche_1)

@app.route("/Kevin")
def attaccante_2():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Kevin Dragonfly'")
      statistiche_2 = mycursor.fetchall()
      return render_template('Kevin.html', statistiche_2=statistiche_2)

@app.route("/Maxwell")
def centrocampista_2():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Maxwell Carson'")
      statistiche_3 = mycursor.fetchall()
      return render_template('Maxwell.html', statistiche_3=statistiche_3)

@app.route("/Nathan")
def centrocampista_sinistro():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Nathan Swift'")
      statistiche_4 = mycursor.fetchall()
      return render_template('Nathan.html', statistiche_4=statistiche_4)

@app.route("/Sam")
def ala_destra():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Sam Kincaid'")
      statistiche_5 = mycursor.fetchall()
      return render_template('Sam.html', statistiche_5=statistiche_5)

@app.route("/Steve")
def ala_sinistra():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Steve Grim'")
      statistiche_6 = mycursor.fetchall()
      return render_template('Steve.html', statistiche_6=statistiche_6)

@app.route("/Tim")
def centrocampista_destro():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Tim Saunders'")
      statistiche_7 = mycursor.fetchall()
      return render_template('Tim.html', statistiche_7=statistiche_7)
      
@app.route("/Jack")
def difensore_1():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Jack Wallside'")
      statistiche_8 = mycursor.fetchall()
      return render_template('Jack.html', statistiche_8=statistiche_8)

@app.route("/Jim")
def difensore_2():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Jim Wraith'")
      statistiche_9 = mycursor.fetchall()
      return render_template('Jim.html', statistiche_9=statistiche_9)

@app.route("/Jude")
def centrocampista_1():
      mycursor.execute("SELECT Team,Position,Element,Kick,Body,Control,Guard,Speed,Stamina,Guts,1st_Move,2nd_Move,3rd_Move,4th_Move FROM INAZUMA_ELEVEN.players WHERE Name = 'Jude Sharp'")
      statistiche_10 = mycursor.fetchall()
      return render_template('Jude.html', statistiche_10=statistiche_10)


