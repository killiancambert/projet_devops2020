FROM python:3

WORKDIR /app

RUN pip install mysql-connector-python
RUN mkdir /app/json

COPY generation.py .
COPY envoie.py .

CMD ["python", "./generation.py", "./envoie.py"]