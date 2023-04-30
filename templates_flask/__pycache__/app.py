from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/players")
def player_list():
      mycursor.execute("SELECT * FROM INAZUMA_ELEVEN.players")
      myresult = mycursor.fetchall()
      return render_template('site.html', players=myresult)