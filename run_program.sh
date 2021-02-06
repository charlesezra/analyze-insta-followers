#!/bin/bash

python3 -m pip install virtualenv
python3 -m venv ./.venv
source .venv/bin/activate
pip install instaloader

echo "=========================================="
read -p "Enter your Instagram username: "  username
echo "Hello, $username"

echo "Enter your Instagram password: (you won't see it, but it's there // just type)"
read -s password

echo "Getting Data from Instagram by using auth credentials ..."
python get_data.py $username $password

echo "Received all data needed for analysis ..."
python analyze.py