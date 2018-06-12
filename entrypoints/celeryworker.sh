#!/usr/bin/env bash

rm celeryworker.pid

celery -A my_app worker -l info