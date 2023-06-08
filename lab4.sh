#!/bin/bash
cd /home/kali/Documents
apt update
apt install -y python3 python3-pip git
git clone https:/github.com/DarkMoos/lab4.git
cd lab4
chmod +wrx lab4.sh
pip3 install -r requirements.txt
