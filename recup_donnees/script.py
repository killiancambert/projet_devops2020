# //La communication entre le mécanisme de lecture des fichiers json et de génération se fera par Socket Python chaque fois qu’un fichier sera disponible

import json
import os
import pymysql


file ='C:/Users/Asus/Documents/devops/projet_devops2020/automate/json/paramunite_1_26-04-2020.json'
json_data=open(file).read()
json_obj = json.loads(json_data)

def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else if type(val) is float:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val

con = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = '',db = 'testdevops',port ='3308')
cursor = con.cursor()

for i, item in enumerate(json_obj):
    numero_unite = validate_string(item.get("numero_unite", None))
    numero_automate = validate_string(item.get("numero_automate", None))
    type_automate = validate_string(item.get("type_automate", None))
    temperature_cuve = validate_string(item.get("temperature_cuve", None))
    temperature_exterieur = validate_string(item.get("temperature_exterieur", None))
    poids_lait_cuve = validate_string(item.get("poids_lait_cuve", None))
    poids_produit_fini = validate_string(item.get("poids_produit_fini", None))
    pH = validate_string(item.get("pH", None))
    K = validate_string(item.get("K", None))
    NaCl = validate_string(item.get("NaCl", None))
    salmonelle = validate_string(item.get("salmonelle", None))
    Ecoli = validate_string(item.get("Ecoli", None))
    listeria = validate_string(item.get("listeria", None))

    cursor.execute("INSERT INTO automate (numero_unite,	numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria) VALUES (%s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s,	%s)", (numero_unite,	numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria))


conn.commit()
conn.close()
