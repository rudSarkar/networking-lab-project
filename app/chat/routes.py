from . import chat
from ..models.users import Users
from ..models.messages import Messages
from flask import render_template, redirect, url_for, session


@chat.route('/chat/<uname>')
def chat_username(uname):
    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))
    elif session.get('user_id'):
        get_user = Users.query.filter_by(username=uname).first()
        if get_user is None:
            return "Bad request", 400
        all_message = Messages.query.all()
        all_user = Users.query.all()
        return render_template('chat.html', username=get_user.username, messages=all_message, users=all_user)


@chat.route('/simple')
def sample():
    t = Messages.query.all()
    return render_template('sample.html', sample=t)


@chat.route('/chats')
def chat():
    if session.get('user_id') is None:
        return redirect(url_for('auth.login'))
    elif session.get('user_id'):
        users = Users.query.all()
        return render_template('chat_list.html', users=users)

