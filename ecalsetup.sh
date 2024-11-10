#!/bin/sh
set -eu -o pipefail # fail on error and report it, debug all lines

sudo -n true
test $? -eq 0 || exit 1 "you should have sudo privilege to run this script"

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11.10
sudo apt install python3-pip

sudo add-apt-repository ppa:ecal/ecal-5.13
sudo apt-get update
sudo apt-get install ecal
sudo apt install python3-ecal5
sudo apt install libc6 libcurl4 libgcc-s1 libhdf5-103 libprotobuf23 libqt5core5a libqt5gui5 libqt5widgets5 libqt5svg5 libstdc++6 sysstat ifstat libqwt-qt5-6 libyaml-cpp0.7

sudo apt install cmake g++ libprotobuf-dev protobuf-compiler

# protoc --version
# libprotoc 3.12.4
# protoc --proto_path=. --python_out=. test.proto
