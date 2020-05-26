# //La communication entre le mécanisme de lecture des fichiers json et de génération se fera par Socket Python chaque fois qu’un fichier sera disponible

from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

import json
import os
import pymysql.cursors

# Récupération du fichier JSON
file ='../automate/json/paramunite_1_19-05-2020.json'
json_data=open(file).read()
json_obj = json.loads(json_data)


# Retourne toutes les valeurs en string
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode("utf8")
        elif type(val) is float:
            #for x in val:
            #   print(x)
            return str(val).encode("utf8")
        else:
            return val

# Connexion à la base de données
conn = pymysql.connect(host='localhost',
                             user='root',
                             port=3308,
                             password='root',
                             db='testdevops',
                             cursorclass=pymysql.cursors.DictCursor)

for value in json_obj.values():
    numero_unite = validate_string(value.get('numero_unite', None))
    numero_automate = validate_string(value.get('numero_automate', None))
    type_automate = validate_string(value.get('type_automate', None))
    temperature_cuve = validate_string(value.get('temperature_cuve', None))
    temperature_exterieur = validate_string(value.get('temperature_exterieur', None))
    poids_lait_cuve = validate_string(value.get('poids_lait_cuve', None))
    poids_produit_fini = validate_string(value.get('poids_produit_fini', None))
    pH = validate_string(value.get('pH', None))
    K = validate_string(value.get('K', None))
    NaCl = validate_string(value.get('NaCl', None))
    salmonelle = validate_string(value.get('salmonelle', None))
    Ecoli = validate_string(value.get('Ecoli', None))
    listeria = validate_string(value.get('listeria', None))
    try:
        with conn.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO 'automate' ('numero_unite',	'numero_automate','type_automate', 'temperature_cuve', 'temperature_exterieur', 'poids_lait_cuve', 'poids_produit_fini', 'pH', 'K', 'NaCl', 'salmonelle', 'Ecoli', 'listeria') VALUES (%s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s,	%s)"
            cursor.execute(sql, (numero_unite,	numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria))
            #  cursor.execute("INSERT INTO automate (numero_unite,	numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria) VALUES (%s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s,	%s)", (numero_unite,	numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria))

        conn.commit()


    finally:
        conn.close()

# Create routes
api.add_resource(validate_string, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
