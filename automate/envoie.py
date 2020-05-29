import socket
import threading
import json
import sched
import time
import mysql.connector
import pathlib
import glob
import os
from mysql.connector import Error

def envoie():
    # Récéption par socket du fichier json (fonctionnel mais docker mysql non fonctionnel)
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((socket.gethostname(), 1234))
    # json = s.recv(1024).decode('utf-8')
    # jsonString = str(json)
    # print(jsonString)

    allJson = glob.glob('json/*.json')
    for x in allJson:
        with open(x) as json_file:
            print("Envoie de la data "+str(x)+" en cours...")
            data = json.load(json_file)
            # Connexion avec la bdd
            connection = mysql.connector.connect(host='127.0.0.1',
                                                 database='devops',
                                                 port='3306',
                                                 user='root',
                                                 password='rootdevops')
            cursor = connection.cursor()
            try:
                # Ajout données récupéré dans les json dans la base de données
                for automate in data:
                    sql_insert_automate = """INSERT INTO data(
                                                numero_unite,
                                                numero_automate,
                                                type_automate,
                                                temperature_cuve,
                                                temperature_exterieur,
                                                poids_lait_cuve,
                                                poids_produit_fini,
                                                pH,
                                                K,
                                                NaCl,
                                                salmonelle,
                                                Ecoli,
                                                listeria,
                                                dateheure
                                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(sql_insert_automate, (
                        automate['numero_unite'],
                        automate['numero_automate'],
                        automate['type_automate'],
                        automate['temperature_cuve'],
                        automate['temperature_exterieur'],
                        automate['poids_lait_cuve'],
                        automate['poids_produit_fini'],
                        automate['pH'],
                        automate['K'],
                        automate['NaCl'],
                        automate['salmonelle'],
                        automate['Ecoli'],
                        automate['listeria'],
                        automate['dateheure']
                    ))
                    connection.commit()
            finally:
                if cursor != None:
                    cursor.close()
                if connection != None:
                    connection.close()
        print("Envoie de la data"+str(x)+"réussi")
        # Suppression du fichier pour éviter de surcharger
        os.remove(x)
        print("Suppression du fichier "+str(x))


while True:
    envoie()
    time.sleep(60)
