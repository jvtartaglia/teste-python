FROM python:3.9.1-slim-buster

RUN mkdir -p /home/app

WORKDIR /home/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP="main.py" FLASK_DEBUG=1 FLASK_ENV=docker