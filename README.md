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

```shell
rudra:networking-lab-project/ (main✗) $ docker build --tag piegon-chat-app .
[+] Building 31.4s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                     0.0s
 => => transferring dockerfile: 37B                                                                                                                      0.0s
 => [internal] load .dockerignore                                                                                                                        0.0s
 => => transferring context: 2B                                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/python:3.9-alpine                                                                                     1.8s
 => [internal] load build context                                                                                                                        0.0s
 => => transferring context: 46.24kB                                                                                                                     0.0s
 => [1/5] FROM docker.io/library/python:3.9-alpine@sha256:fb0175fbe632a14af6eedf9ae113171d748ebb3ca721be874b99109aac48f06b                               9.6s
 => => resolve docker.io/library/python:3.9-alpine@sha256:fb0175fbe632a14af6eedf9ae113171d748ebb3ca721be874b99109aac48f06b                               0.0s
 => => sha256:fb0175fbe632a14af6eedf9ae113171d748ebb3ca721be874b99109aac48f06b 1.65kB / 1.65kB                                                           0.0s
 => => sha256:ff3b837a015b452b4d8a23abc3f741c1c10ae75247e9ef6536d20cfeea292977 1.37kB / 1.37kB                                                           0.0s
 => => sha256:6c0d09aae0eaf98a93065b9e63645c2376d71a0cece341e9023e19c90d7f6366 7.05kB / 7.05kB                                                           0.0s
 => => sha256:40e059520d199e1a1a259089077f2a0c879951c9a4540490bad3a0d7714c6ae7 2.81MB / 2.81MB                                                           2.1s
 => => sha256:4f950178bcecafaa0400ab3ea61cc27fd35a495600946da9fe805e2a46caa955 667.02kB / 667.02kB                                                       2.2s
 => => sha256:1cef3ccb17b1abf33ecdcdc2ecf7710610cb273a4dc2ffde4f8e82e0cd96c074 12.06MB / 12.06MB                                                         8.0s
 => => extracting sha256:40e059520d199e1a1a259089077f2a0c879951c9a4540490bad3a0d7714c6ae7                                                                0.3s
 => => sha256:d0e4775ea75164656211321ce39852b910713f7e7e96b6e58668ecba28a688d8 233B / 233B                                                               2.5s
 => => sha256:c7e4802b9301433ca310b38204c0fec570be4970bb802a53d958410366d4c0e2 2.87MB / 2.87MB                                                           5.5s
 => => extracting sha256:4f950178bcecafaa0400ab3ea61cc27fd35a495600946da9fe805e2a46caa955                                                                0.4s
 => => extracting sha256:1cef3ccb17b1abf33ecdcdc2ecf7710610cb273a4dc2ffde4f8e82e0cd96c074                                                                0.9s
 => => extracting sha256:d0e4775ea75164656211321ce39852b910713f7e7e96b6e58668ecba28a688d8                                                                0.0s
 => => extracting sha256:c7e4802b9301433ca310b38204c0fec570be4970bb802a53d958410366d4c0e2                                                                0.4s
 => [2/5] WORKDIR /networking-lab-project                                                                                                                0.1s
 => [3/5] COPY requirements.txt requirements.txt                                                                                                         0.0s
 => [4/5] RUN pip3 install -r requirements.txt                                                                                                          19.2s
 => [5/5] COPY . .                                                                                                                                       0.0s
 => exporting to image                                                                                                                                   0.5s
 => => exporting layers                                                                                                                                  0.5s
 => => writing image sha256:28909a3357e0f6b4f310625439fc5e1f413a039ad8b501a24f678b4b526f1ae6                                                             0.0s
 => => naming to docker.io/library/piegon-chat-app                                                                                                       0.0s
```

Then create docker container and run in detached mode from the docker image are exists we've built pasting following command

```shell
$ docker run --name piegon-chat-continer -d -p 80:5000 piegon-chat-app
```

```shell
rudra:networking-lab-project/ (main✗) $ docker run --name piegon-chat-continer -d -p 80:5000 piegon-chat-app
329a50c42abeb1ecc8341bbee714853124908312eba45f809b286a62ee09b8b7
```

Now the container can be accessible from http://public-ip-or-dns.com/