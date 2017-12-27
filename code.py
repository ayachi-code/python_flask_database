#importeer mysqldb
import MySQLdb


#importeer FLask
from flask import *
app = Flask(__name__)


#als iemand naar / gaat
@app.route('/')
def laat_home_zien():
    return render_template("home.html")



@app.route('/verzenden/<bericht>')
def verstuur_bericht(bericht):
    return "test"



app.run()
