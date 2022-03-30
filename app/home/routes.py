from flask import render_template
from . import home
from .. import mysql

@home.route('/')
def index():
	# cur = mysql.connection.cursor()
	# cur.execute("""SELECT user, host FROM mysql.user""")
	# rv = cur.fetchall()
	name = "Rudra Sarkar"
	return render_template('index.html', name=name)