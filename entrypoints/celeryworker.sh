#!/usr/bin/env bash

rm celeryworker.pid

celery -A main_application worker -l info --logfile=/log/celery_worker.log