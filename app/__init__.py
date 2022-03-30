from .config import DevConfig, ProdConfig
import MySQLdb.cursors
from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*")
mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = DevConfig.SECRET_KEY

    # database configuration
    app.config['MYSQL_HOST'] = DevConfig.MYSQL_HOST
    app.config['MYSQL_USER'] = DevConfig.MYSQL_USER
    app.config['MYSQL_PASSWORD'] = DevConfig.MYSQL_PASSWORD
    app.config['MYSQL_DB'] = DevConfig.MYSQL_DB

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

    # initiate mysql
    mysql.init_app(app)

    return app