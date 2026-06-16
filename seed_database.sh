#!/bin/bash

rm db.sqlite3
rm -rf ./escapeapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations escapeapi
python3 manage.py migrate escapeapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

