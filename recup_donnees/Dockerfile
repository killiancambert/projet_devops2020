FROM python:3

WORKDIR /app

RUN pip install mysql-connector-python
RUN pip install flask
RUN pip install flask_cors
RUN pip install mariadb

COPY script.py .
COPY python_dump.py .

CMD ["python", "./script.py", "python_dump.py"]