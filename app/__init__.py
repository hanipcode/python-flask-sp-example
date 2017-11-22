from flask import Flask
from flask.ext.mysql import MySQL 


app = Flask(__name__)
mysql = MySQL()
app.config.from_object('config')
mysql.init_app(app)

from app import views