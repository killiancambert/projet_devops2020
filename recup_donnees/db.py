import pymysql


def connect():
    return pymysql.connect(host='db', port=3306, user='root', password='root', db='devops', cursorclass=pymysql.cursors.DictCursor)


address = "0.0.0.0"
port = 1111
