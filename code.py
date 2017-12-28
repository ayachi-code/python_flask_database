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
    cur.execute("INSERT INTO gegevens(naam,bericht) VALUES(%s,%s)", (naam,bericht))
    database_connectie.commit()
    return render_template("gelukt.html",persoon_naam=naam,persoon_bericht=bericht)



#als iemand naar zien gaat
@app.route('/zien')
def zien():
    #execute query
    cur.execute("SELECT * FROM gegevens")
    #fetch gegevens
    gegevens = cur.fetchall()
    for rij in gegevens:
        print(rij[0])
    #render template
    return render_template("zien.html")



app.run(host="192.168.178.185",port=3000)


#sluiten...
cur.close()
database_connectie.close()
