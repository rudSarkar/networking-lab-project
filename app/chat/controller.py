from flask import session
from ..models.users import Users


def save_message(current_user, logged_user):
    pass


def get_messages(current_user, logged_user):
    print(f'{current_user} and {logged_user} talking with each other and we gotta query and fetch out the message')
