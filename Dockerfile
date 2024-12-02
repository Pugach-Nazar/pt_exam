# FROM python:3.11
FROM alpine

RUN apk add --update python3 py-pip

WORKDIR /app

COPY . /app

CMD [ "python", "exam.py"]