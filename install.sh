#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python3 and pip..."
    sudo apt-get update
    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y
fi

pip3 install pyyml
sudo apt-get install curl -y

curl https://raw.githubusercontent.com/omidima/omidocker/main/omidocker > omidocker
sudo mv omidocker /bin/omidocker
sudo chmod +x /bin/omidocker
