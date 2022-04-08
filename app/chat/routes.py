from . import chat
from ..extensions import db
from ..models.users import Users
from flask import render_template, redirect, url_for, request, flash, Markup, session


@chat.route('/chat/<uname>')
def chat_username(uname):
	if session.get('user_id') is None:
		return redirect(url_for('auth.login'))
	elif session.get('user_id'):
		return render_template('users.html', uname=uname)


@chat.route('/chats')
def chat():
	if session.get('user_id') is None:
		return redirect(url_for('auth.login'))
	elif session.get('user_id'):
		users = Users.query.all()
		return render_template('users.html', users=users)
