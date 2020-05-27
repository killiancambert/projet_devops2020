# //La communication entre le mécanisme de lecture des fichiers json et de génération se fera par Socket Python chaque fois qu’un fichier sera disponible

from flask import Flask
from flask import request
from flask_cors import CORS
import mysql.connector as mariadb
from mysql.connector import Error
import datetime
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["DEBUG"] = True


def getDate(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.timestamp()


@app.route('/unites/all', methods=['GET'])
def get_all_unites():
    mariadb_connection = mariadb.connect(host='localhost',
                                         database='devops',
                                         port='3306',
                                         user='root',
                                         password='rootdevops')
    cursor = mariadb_connection.cursor()
    try:
        sql = "SELECT * FROM `data`"
        cursor.execute(sql)
        return (app.response_class(
            response=json.dumps(cursor.fetchall(), default=getDate),
            status=200,
            mimetype='application/json'
        ))
    finally:
        if cursor != None:
            cursor.close()
        if mariadb_connection != None:
            mariadb_connection.close()

    return (app.response_class(
            response=json.dumps({}, default=getDate),
            status=200,
            mimetype='application/json'
            ))

@app.route('/', methods=['GET'])
def home():
    return "<h1>DATA API</h1><p>Acces à toutes les data des unites et leurs automates.</p>"


if __name__ == '__main__':
    app.run(debug=True)
