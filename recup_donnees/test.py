import pymysql.cursors
import random

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             port=3308,
                             password='',
                             db='testdevops',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with conn.cursor() as cursor:
        numero_unite = 1
        numero_automate = 1
        while numero_unite < 6:
            while numero_automate < 11:
                
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
                # Create a new record
                sql = "INSERT INTO `automate` (`numero_unite`, `numero_automate`, `type_automate`, `temperature_cuve`, `temperature_exterieur`, `poids_lait_cuve`, `poids_produit_fini`, `pH`, `K`, `NaCl`, `salmonelle`, `Ecoli`, `listeria`) VALUES (%s,%s,%s, %s,%s,	%s, %s,	%s,	%s, %s,	%s,	%s,	%s)"
                cursor.execute(sql, (numero_unite,	numero_automate,"0X0000BA20", temperature_cuve, temperature_exterieur, poids_lait_cuve, poids_produit_fini, pH, K, NaCl, salmonelle, Ecoli, listeria))
                numero_automate += 1

            numero_automate= 1
            numero_unite += 1


            conn.commit()


finally:
    conn.close()
