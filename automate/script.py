# //Chaque unité de production produira toute les minutes un fichier Json unique comportant des informations fixes ou générées aléatoirement

# //Son nom sera constitué de: paramunite _< numéro unité >_<date unix epoch>.json

# //Python 3.7.x

import json
from datetime import datetime
import random

today = datetime.now()
date = today.strftime("%d-%m-%Y")

numero_unite = 1

while numero_unite < 6:

    json_name = "json/paramunite_{}_{}.json".format(numero_unite, date)

    numero_automate = 1

    data = {}
    data['data'] = []
    while numero_automate < 11:
        type_automate = ['0X0000BA20', '0X0000BA2F']
        temperature_cuve = round(random.uniform(2.5, 4), 1)
        temperature_exterieur = round(random.uniform(8, 14), 1)
        poids_lait_cuve = random.randint(3512, 4607)
        poids_produit_fini = 1
        pH = round(random.uniform(6.8, 7.2), 1)
        K = random.randint(35, 47)
        NaCl = round(random.uniform(1, 1.7), 1)
        salmonelle = random.randint(17, 37)
        Ecoli = random.randint(35, 49)
        listeria = random.randint(28, 54)
        data['data'].append({
            'numero_unite': numero_unite,
            'numero_automate': numero_automate,
            'type_automate': random.choice(type_automate),
            'temperature_cuve': temperature_cuve,
            'temperature_exterieur': temperature_exterieur,
            'poids_lait_cuve': poids_lait_cuve,
            'poids_produit_fini': poids_produit_fini,
            'pH': pH,
            'K': K,
            'NaCl': NaCl,
            'salmonelle': salmonelle,
            'Ecoli': Ecoli,
            'listeria': listeria
        })
        numero_automate += 1

    numero_automate= 1

    with open(json_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    numero_unite += 1

numero_automate = 1
