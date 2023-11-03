#!/bin/bash
if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python3 and pip..."
    sudo apt-get update
    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y
fi

pip3 install pyyml
sudo apt-get install curl -y

curl https://raw.githubusercontent.com/omidima/omidocker/main/omidocker.py > omidocker.py
sudo mv omidocker.py /var/omidocker.py

echo "alias omidocker='python3 /var/omidocker.py'" >> ~/.bashrc 
echo "alias omidocker='python3 /var/omidocker.py'" >> ~/.zshrc 
echo "alias omidocker='python3 /var/omidocker.py'" >> ~/.bash_profile 

source ~/.bashrc 
source ~/.zshrc 
source ~/.bash_profile 