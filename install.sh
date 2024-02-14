#!/bin/bash

./cfg.sh

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

touch FLASK_DATABASE
sqlite3 FLASK_DATABASE < facereference/schema.sql