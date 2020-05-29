FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /recup_donnees
WORKDIR /recup_donnees
COPY requirements.txt /recup_donnees/
RUN pip3 install -r requirements.txt

COPY . /recup_donnees/