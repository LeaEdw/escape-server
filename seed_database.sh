rm db.sqlite3
rm -rf ./escapeapi/migrations
python3 manage.py makemigrations escapeapi
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata locations
python3 manage.py loaddata games
python3 manage.py loaddata game_images
python3 manage.py loaddata reactions
python3 manage.py loaddata ratings