import os
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from .config import DevConfig, ProdConfig

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = DevConfig.SECRET_KEY

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_database.db'

    # importing blueprint
    from .home import home as home_blueprint
    from .chat import chat as chat_blueprint
    from .auth import auth as auth_blueprint

    # register blueprint
    app.register_blueprint(chat_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)

    # initiate socket
    socketio.init_app(app)

    # enable CORS origin
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app