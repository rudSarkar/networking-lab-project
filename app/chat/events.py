from .. import socketio
from .controller import *


@socketio.on('joined_chat')
def joined(data):
    print(f"{data['current_user']} start chatting with {data['chat_user']}.")


@socketio.on('send_message')
def send_message(data):
    print(f"{data['current_user']} sent '{data['message']}' to {data['chat_user']}")
    """ Save message to database """

    socketio.emit('received_message', data, target_chat_user=data['chat_user'])
    get_messages(data['current_user'], data['chat_user'])
