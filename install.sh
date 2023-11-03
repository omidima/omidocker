#!/bin/bash

pip install pyyml
sudo cp omidocker.py /var/omidocker.py

echo 'alias omidocker="python /var/omidocker.py"' >> ~/.zshrc
source ~/.zshrc

echo 'alias omidocker="python /var/omidocker.py"' >> ~/.bashrc
source ~/.bashrc