#!/usr/bin/env bash

rm celeryworker.pid

celery flower -A my_app --port=5555