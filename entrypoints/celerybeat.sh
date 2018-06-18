#!/usr/bin/env bash

rm celerybeat.pid

celery -A main_application beat -S django -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler --logfile=/log/celery_beat.log