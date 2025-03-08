FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY requirements* manage.py app/ project/ .

RUN pip install gunicorn && pip install -r requirements.txt
