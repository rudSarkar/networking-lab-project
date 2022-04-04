# Messaging Application
This project created for Networking Lab course, This is a messaging application built with Python, Flask, Flask-SocketIO, Socket.io

### How to setup

* .env
* More will be added here

### Requirements

* Python 3.7+
* Flask
* More will be added here

### Run with docker

First build docker image which tag is piegon-chat-app :

```bash
$ docker build --tag piegon-chat-app . -d
```

Then create docker container and run in detached mode from the docker image are exists we've built pasting following command

```shell
$ docker run -d -p 80:5000 piegon-chat-app
```

Now the container can be accessible from http://public-ip-or-dns.com/