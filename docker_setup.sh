#!/bin/sh
sudo apt-get update
sudo apt-get -y install podman
sudo apt install -y docker.io
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
code --install-extension ms-vscode-remote.remote-containers
