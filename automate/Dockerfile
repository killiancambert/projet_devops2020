FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /automate
WORKDIR /automate
COPY requirements.txt /automate/
RUN pip3 install -r requirements.txt

COPY . /automate/