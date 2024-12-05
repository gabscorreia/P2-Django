pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
cp db.sqlite3 /tmp/db.sqlite3