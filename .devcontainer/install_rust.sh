#!/bin/bash

# Download and run the Rust installation script
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Source the Cargo environment
. "$HOME/.cargo/env"

# Verify installation
if command -v rustc >/dev/null 2>&1; then
    echo "Rust installed successfully"
    rustc --version
    cargo --version
else
    echo "Rust installation failed"
    exit 1
fi