from flask import render_template
from . import auth

@auth.route('/login')
def login():
	return render_template('login.html')


@auth.route('/signup')
def signup():
	return render_template('signup.html')