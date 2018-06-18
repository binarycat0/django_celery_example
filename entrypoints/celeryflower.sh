#!/usr/bin/env bash

rm celeryworker.pid

celery flower -A main_application --port=5555 --logging=info -log-file-prefix=/log/flower.log