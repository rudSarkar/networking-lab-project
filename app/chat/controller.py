from flask import session
from ..models.messages import Messages
from ..extensions import db


def save_message(current_user, message):
    pass_message_value = Messages(
        current_user=current_user,
        message=message
    )
    db.session.add(pass_message_value)
    db.session.commit()


def get_messages(current_user, logged_user):
    print(Messages.query.filter_by(current_user=current_user, chat_user=logged_user).first())
