import re
from . import auth
from ..models.users import Users
from ..extensions import db, bcrypt
from flask import render_template, redirect, url_for, request, flash, Markup


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        test = "nano"
        return 'POST Login', 200

    return render_template('login.html'), 200


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['fullname']
        user_name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        pwd_hash = bcrypt.generate_password_hash(password)

        email_exists = Users.query.filter_by(email=email).first()
        username_exists = Users.query.filter_by(username=user_name).first()

        if full_name == "" or user_name == "" or email == "" or password == "":
            flash('Data required in the form', category='danger')
        else:
            if email_exists:
                flash('Email address already exists', category='danger')
                return redirect(url_for('auth.signup'))
            if username_exists:
                flash('Username already exists', category='danger')
                return redirect(url_for('auth.signup'))
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email address', category='warning')
                return redirect(url_for('auth.signup'))
            if not re.match(r'[A-Za-z0-9]+', user_name):
                flash('Username must contain only characters and numbers', category='warning')
                return redirect(url_for('auth.signup'))
            if not re.match(r'[A-Za-z0-9 ]+', full_name):
                flash('Full name must contain only characters, numbers and space', category='warning')
                return redirect(url_for('auth.signup'))

            create_user = Users(
                fullname=full_name,
                username=user_name,
                email=email,
                password=pwd_hash
            )

            db.session.add(create_user)
            db.session.commit()

            flash(Markup('Account created. Click on <a href="/login">Login</a>'), category='success')
            return redirect(url_for('auth.signup')), 201

    return render_template('signup.html'), 200
