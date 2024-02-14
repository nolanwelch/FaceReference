#!/bin/bash

echo Beginning install ...
sleep 1

source cfg.sh
echo Loaded config.

echo Creating virtual environment ...
python3 -m venv env
source env/bin/activate

echo Upgrading pip ...
pip install --upgrade pip

echo Installing from requirements.txt ...
pip install -r requirements.txt

echo Initializing database ...
touch $FLASK_DATABASE
sqlite3 $FLASK_DATABASE < facereference/schema.sql

echo Done!
rm -- "$0"

exit