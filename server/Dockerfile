# Dockerfile
FROM python:3.9.10-alpine3.14
WORKDIR /server
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt