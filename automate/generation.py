import random
from datetime import datetime
import time
import json
import sys
import os
import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)

id_unite = os.getenv('UNITE')

if id_unite == None:
    id_unite = [1, 2, 3, 4, 5]

# Définir le nombre d'unité et d'automate souhaité
nombre_unite = 5
nombre_automate = 10

# Liste pour séléctionner aléatoirement le type d'automate
random_type = ['0X0000BA20', '0X0000BA2F']


today = datetime.now()
date = today.strftime("%d-%m-%Y")


def generation():
    for x in id_unite:
        json_name = "paramunite_"+str(x)+"_"+str(date)+".json"
        print("Creation fichier {}".format(json_name))
        data = []
        for y in range(1, nombre_automate + 1):
            type_automate = random.choice(random_type)
            temperature_cuve = round(random.uniform(2.5, 4), 1)
            temperature_exterieur = round(random.uniform(8, 14), 1)
            poids_lait_cuve = random.randint(3512, 4607)
            poids_produit_fini = 4607 - random.randint(3512, 4607)
            pH = round(random.uniform(6.8, 7.2), 1)
            K = random.randint(35, 47)
            NaCl = round(random.uniform(1, 1.7), 1)
            salmonelle = random.randint(17, 37)
            Ecoli = random.randint(35, 49)
            listeria = random.randint(28, 54)
            dateheure = today.strftime("%d-%m-%Y %H:%M:%S")
            data.append({
                'numero_unite': x,
                'numero_automate': y,
                'type_automate': type_automate,
                'temperature_cuve': temperature_cuve,
                'temperature_exterieur': temperature_exterieur,
                'poids_lait_cuve': poids_lait_cuve,
                'poids_produit_fini': poids_produit_fini,
                'pH': pH,
                'K': K,
                'NaCl': NaCl,
                'salmonelle': salmonelle,
                'Ecoli': Ecoli,
                'listeria': listeria,
                'dateheure': dateheure
            })
        with open('json/'+json_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Fichier %s créé" % json_name)

    # Socket qui envoie le nom json au serveur (fonctionnel mais docker mysql non fonctionnel)
    # print('Envoie json au serveur')
    # clientsocket, address = s.accept()
    # print(f"Connexion depuis {address} a été établite !")
    # clientsocket.send(bytes(json_name, 'utf-8'))
    # clientsocket.close()

    print("\nLe prochain fichier sera créé dans 60 secondes.")

while True:
    generation()
    time.sleep(60)
