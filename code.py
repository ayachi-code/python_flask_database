#importeer mysqldb
import MySQLdb

#connecteren met database
database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="almujaahid/0",db="berichten")
cur = database_connectie.cursor()

#importeer FLask
from flask import *
app = Flask(__name__)


#als iemand naar / gaat
@app.route('/')
def laat_home_zien():
    return render_template("home.html")


#Als iemand een bericht gaat versturen
@app.route('/verzenden/<naam>/<bericht>')
def verstuur_bericht(naam,bericht):
    pass




app.run()
