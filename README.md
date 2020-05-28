# Projet DevOps 2020

- Killian Cambert : killiancambert
- Antonin Joulie : AntoninJoulie
- Valentin Dezat : valdezat

# Lancer le projet en local

Pour lancer les programmes python en local, il va vous falloir 4 invite de commande.

Voici tout d'abord les dépendances nécessaires :

`python -m pip install mysql-connector-python`
`python -m pip install flask`
`python -m pip install flask_cors`

Parcourez les fichiers pour entrer dans le document 'automate' puis lancez la commande suivante :

`python generation.py`

Ce programme permet de créer les json à l'aide des 5 unités composé de 10 automates.

Puis dans le même document lancez une seconde invite de commande avec la commande suivante :

`python envoie.py`

Ce script permet derécupérer les fichier json et de les saisir dans la base de données.

Lancé dans cet ordre, les deux scripts se lanceront toutes les minutes.

Pour la troisième invite de commande, entrez dans le document 'recup_donnees' et lancez la commande suivante :

`python script.py`

Ce programme lancera une interface web : http://127.0.0.1:5000/ où on peut retrouver les données de la base.

Le dernier script est dans le document 'recup_donnees' :

`python python_dump.py`

Ce programme permet de créer un dump de la base avec les données actuelles.

# Comment lancer Docker

Il faut éxécuter cette commande :

`docker compose up`

# Pour lancer la partie web

Il faut se placer sur la partie **plateforme** grâce à cette commande :

`cd plateforme`

Il faut utiliser l'extension **Live Server** dans Visual Studio Code

Ensuite pour lancer Live Server, il est possible d'appuyer sur le bouton **Go Live** qui se situe en bas à droite de la fenêtre Visual Studio Code.

Une fois cela fait, la plateforme sera lancée automatiquement sur une page localhost
