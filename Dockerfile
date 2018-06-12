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

