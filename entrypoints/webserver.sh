#!/usr/bin/env bash

_term() {
  echo "Caught SIGTERM signal!"
  kill -TERM "$child" 2>/dev/null
}

trap _term SIGTERM

echo "HELLO!"

sleep 10

python3 manage.py migrate auth
python3 manage.py migrate main_application
python3 manage.py migrate django_celery_results
python3 manage.py migrate django_celery_beat
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py shell -c "from django.contrib.auth.models import User; print('admin already exist') if User.objects.filter(username='admin').exists() else User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty123456')"
python3 manage.py runserver 0.0.0.0:$PORT

child=$!
wait "$child"