from app import create_app, socketio, mysql

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)