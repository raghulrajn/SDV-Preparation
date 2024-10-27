#!/bin/sh
sudo apt install -y docker.io
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
