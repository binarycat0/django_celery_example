# How to use Django with celery

## Required:

- docker >= 1.13
    - [Mac OS](https://docs.docker.com/docker-for-mac/install/)
    - [Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)
    - [Centos](https://docs.docker.com/install/linux/docker-ce/centos/#install-docker-ce)
- docker-compose
    - [Install Docker Compose](https://docs.docker.com/compose/install/)

## docker-compose file
```yaml
version: "3"

services:

  nginx:
    image: nginx:latest
    volumes:
     - ./nginx.conf:/etc/nginx/conf.d/nginx.conf
     - /log
     - static:/static
     - media:/media
    ports:
     - "80:80"
    environment:
     - NGINX_PORT=80
    links:
      - django
    depends_on:
      - django
    command: /bin/bash -c "envsubst < /etc/nginx/conf.d/nginx.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"


  django:
    hostname: "django"
    build: .
    image: "django_celery_example"
    restart: "always"
    entrypoint: /entrypoints/webserver.sh
    env_file:
      - django_env_file
    volumes:
      - ./src:/app
      - ./entrypoints:/entrypoints
      - /log
      - static:/static
      - media:/media
    links:
      - db
      - redis
    depends_on:
      - db
      - redis

  celery_worker:
    image: "django_celery_example"
    restart: "always"
    entrypoint: /entrypoints/celeryworker.sh
    env_file:
      - django_env_file
    volumes:
      - ./src:/app
      - ./entrypoints:/entrypoints
      - /log
    links:
      - db
      - redis
      - django
    depends_on:
      - django

  celery_beat:
    image: "django_celery_example"
    restart: "always"
    entrypoint: /entrypoints/celerybeat.sh
    env_file:
      - django_env_file
    volumes:
      - ./src:/app
      - ./entrypoints:/entrypoints
      - /log
    links:
      - db
      - redis
      - django
    depends_on:
      - django

  celery_flower:
    image: "django_celery_example"
    restart: "always"
    entrypoint: /entrypoints/celeryflower.sh
    env_file:
      - django_env_file
    volumes:
      - ./src:/app
      - ./entrypoints:/entrypoints
      - /log
    links:
      - redis
      - django
      - celery_worker
      - celery_beat
    depends_on:
      - django
      - celery_beat
      - celery_worker
    ports:
      - 5555:5555

  db:
    hostname: "db"
    image: "postgres:9.6"
    env_file:
      - django_env_file
    volumes:
      - db_data:/var/lib/postgresql/data

  redis:
    hostname: "redis"
    image: "redis"
    volumes:
      - redis_data:/data
    depends_on:
      - db

volumes:
  db_data:
  redis_data:
  nginx_log:
  static:
  media:
```

## Docker file
```yaml
FROM python:3.6

RUN mkdir /app
RUN mkdir /entrypoints

COPY ./src /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY ./entrypoints/celerybeat.sh /entrypoints
COPY ./entrypoints/celeryworker.sh /entrypoints
COPY ./entrypoints/webserver.sh /entrypoints

RUN chmod +x /entrypoints/celerybeat.sh
RUN chmod +x /entrypoints/celeryworker.sh
RUN chmod +x /entrypoints/webserver.sh

RUN mkdir /media/upload

ENV PORT=8000
EXPOSE $PORT
```

## build
sudo docker-compose build

## start
sudo docker-compose up

## stop
sudo docker-compose stop

## remove
sudo docker-compose down --rmi=local
sudo docker volume prune
