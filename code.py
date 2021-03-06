#importeer mysqldb
import MySQLdb
from itertools import chain

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
    cur.execute("INSERT INTO gegevens(naam,bericht) VALUES(%s,%s)", (naam,bericht))
    database_connectie.commit()
    return render_template("gelukt.html",persoon_naam=naam,persoon_bericht=bericht)

#Als er een 404 optreed
@app.errorhandler(404)
def error(e):
    return render_template("error.html")



app.run(host="192.168.178.185",port=3000)


#sluiten...
cur.close()
database_connectie.close()
