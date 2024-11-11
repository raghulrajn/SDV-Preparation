#!/bin/sh
set -eu -o pipefail # fail on error and report it, debug all lines

# Function to log errors
log_error() {
  echo "[ERROR] $1"
  errors="$errors$1\n"
}

# Initialize errors variable to store any failed installations
errors=""

# Check if the user has sudo privileges
sudo -n true
if test $? -ne 0; then
  log_error "You should have sudo privilege to run this script"
  exit 1
fi

# Install dependencies
{
  # Add repositories and install python3.11 and pip
  sudo add-apt-repository ppa:deadsnakes/ppa -y || log_error "Failed to add deadsnakes PPA"
  sudo apt update || log_error "Failed to update package list"

  # Add eCAL repository and install eCAL
  sudo add-apt-repository ppa:ecal/ecal-5.13 -y || log_error "Failed to add eCAL repository"
  sudo apt-get update || log_error "Failed to update package list"
  sudo apt-get install -y ecal || log_error "Failed to install eCAL"
  sudo apt install -y python3-ecal5 || log_error "Failed to install python3-ecal5"
  
  # Install required libraries
  sudo apt install -y libc6 libcurl4 libgcc-s1 libhdf5-103 libprotobuf23 libqt5core5a libqt5gui5 libqt5widgets5 libqt5svg5 libstdc++6 sysstat ifstat libqwt-qt5-6 libyaml-cpp0.7 || log_error "Failed to install required libraries"

  # Install cmake, g++, and protobuf dependencies
  sudo apt install -y cmake g++ libprotobuf-dev protobuf-compiler || log_error "Failed to install cmake, g++, and protobuf dependencies"
} || log_error "An installation error occurred"

# Check if any errors occurred and report them
if [ -n "$errors" ]; then
  echo -e "The following errors occurred during installation:\n$errors"
  exit 1
else
  echo "All packages installed successfully!"
fi


# protoc --version
# libprotoc 3.12.4
# protoc --proto_path=. --python_out=. test.proto
