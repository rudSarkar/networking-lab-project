import re
from . import auth
from ..models.users import Users
from flask import render_template, redirect, url_for, request, flash


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html'), 200
    elif request.method == "POST":
        test = "nano"
        return 'POST Login', 200
    else:
        return 'Something went wrong or this method is\'t allowed', 405


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['fullname']
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = Users.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        create_user = Users(
            fullname=full_name,
            username=user_name,
            email=email,
            password=password
        )
    return render_template('signup.html'), 200
