from . import chat
from ..models.users import Users
from flask import render_template, redirect, url_for, request, flash, Markup, session


@chat.route('/chat/<uname>')
def chat_username(uname):
    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))
    elif session.get('user_id'):
        get_user = Users.query.filter_by(username=uname).first()
        if get_user is None:
            return "Bad request", 400
        return render_template('chat.html', username=get_user.username)


@chat.route('/chats')
def chat():
    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))
    elif session.get('user_id'):
        users = Users.query.all()
        return render_template('chat_list.html', users=users)
