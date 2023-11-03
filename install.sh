#!/bin/bash

pip install pyyml
sudo apt-get install curl -y

curl https://raw.githubusercontent.com/omidima/omidocker/main/omidocker.py > omidocker.py
sudo mv omidocker.py /var/omidocker.py

echo "alias omidocker='python /var/omidocker.py'" >> ~/.bashrc 
echo "alias omidocker='python /var/omidocker.py'" >> ~/.zshrc 
echo "alias omidocker='python /var/omidocker.py'" >> ~/.bash_profile 

source ~/.bashrc 
source ~/.zshrc 
source ~/.bash_profile 