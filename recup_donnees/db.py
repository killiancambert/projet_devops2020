# //La communication entre le mécanisme de lecture des fichiers json et de génération se fera par Socket Python chaque fois qu’un fichier sera disponible

import mysql.connector as MC
# from flask import Flask
# from flask_restful import Resource, Api

# # Instantiate the app
# app = Flask(__name__)
# api = Api(app)


def insert_data():
    try:
        conn = MC.connect(host='localhost', user='root', password='root', database='devops')
        cursor = conn.cursor()

        req = 'INSERT INTO data(numero_unite, numero_automate,type_automate, temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria) VALUES(%s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s, %s,	%s,	%s,	%s)'
        infos = (1, 1, '0X0000BA20', 2.8, 8.1, 4368, 1, 6.9, 38, 1.4, 25, 45, 39)

        cursor.execute(req, infos)
        conn.commit()

        req  = 'SELECT * FROM data'
        cursor.execute(req)

        alldonnees = cursor.fetchall()

        for donnees in alldonnees:
            print('Numéro unité : {}'.format(donnees[1]), 'Numéro automate : {}'.format(donnees[2]), 'Type d`automate : {}'.format(donnees[3]), 'Température cuve : {}'.format(donnees[4]), 'Température exterieur : {}'.format(donnees[5]), 'Poids du lait en cuve : {}'.format(donnees[6]), 'Poids du produit fini réalisé : {}'.format(donnees[7]), 'Mesure pH : {}'.format(donnees[8]), 'Mesure K+ : {}'.format(donnees[9]), 'Concentration de NaCl : {}'.format(donnees[10]), 'Niveau bactérien salmonelle : {}'.format(donnees[11]), 'Niveau bactérien E-coli : {}'.format(donnees[12]), 'Niveau bactérien listeria : {}'.format(donnees[13]))

        #fetchone, fetchall, fetchmany
    except MC.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()


insert_data()


# # Create routes
# api.add_resource(insert_data, '/')

# # Run the application
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True)
