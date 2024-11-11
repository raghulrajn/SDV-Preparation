#!/bin/bash

set -e  # Exit on any error

# Update and install dependencies
echo "Updating system and installing dependencies..."
sudo apt update
sudo apt install -y build-essential autoconf libtool pkg-config cmake git

# Check if Protobuf is already installed
if command -v protoc >/dev/null 2>&1; then
    echo "Protobuf is already installed at: $(which protoc)"
else
    # Install Protobuf
    echo "Cloning and installing Protobuf..."
    PROTOBUF_VERSION="v3.21.12"
    git clone -b $PROTOBUF_VERSION https://github.com/protocolbuffers/protobuf.git
    cd protobuf
    mkdir -p cmake/build
    cd cmake/build
    cmake ../.. -DBUILD_SHARED_LIBS=ON -Dprotobuf_BUILD_TESTS=OFF  # Disable tests
    make -j$(nproc)
    sudo make install
    sudo ldconfig  # Update linker cache
    cd ../../..  # Go back to the root directory
    rm -rf protobuf  # Clean up Protobuf source files
fi

# Check if gRPC is already installed
if command -v grpc_cpp_plugin >/dev/null 2>&1; then
    echo "gRPC is already installed at: $(which grpc_cpp_plugin)"
else
    # Install gRPC
    echo "Cloning and installing gRPC..."
    GRPC_VERSION="v1.48.0"
    git clone -b $GRPC_VERSION https://github.com/grpc/grpc.git
    cd grpc
    git submodule update --init --recursive  # Initialize gRPC submodules
    mkdir -p cmake/build
    cd cmake/build
    cmake ../.. -DBUILD_SHARED_LIBS=ON -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF
    make -j$(nproc)
    sudo make install
    sudo ldconfig  # Update linker cache
    cd ../../..  # Go back to the root directory
    rm -rf grpc  # Clean up gRPC source files
fi

# Verify installations
echo "Verifying installation..."
if command -v grpc_cpp_plugin >/dev/null 2>&1 && command -v protoc >/dev/null 2>&1; then
    echo "gRPC and Protobuf installed successfully."
    echo "grpc_cpp_plugin located at: $(which grpc_cpp_plugin)"
    echo "protoc located at: $(which protoc)"
else
    echo "Error: Installation failed. grpc_cpp_plugin or protoc not found."
    exit 1
fi

echo "Installation complete."

