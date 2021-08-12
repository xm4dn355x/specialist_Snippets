release: python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn Snippets.wsgi --log-file -
