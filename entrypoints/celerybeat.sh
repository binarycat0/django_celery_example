#!/usr/bin/env bash

rm celerybeat.pid

celery -A my_app beat -S django -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler