# Projet Photomosaïque

Ce projet a été donné en mars 2021 à un groupe d'élèves de terminale NSI.
Il est actuellement en *work in progress*.

Les documents proposés ici sont ma version de ce projet que je mène en parallèle du travail de mes élèves.

## Mots-clefs :

Python, PIL, CSV, Base de données

## Les différentes étapes

1. Première étape : *Fait* <br />
Créer une mosaïque d'une photo en créer des carrés ayant pour couleur la couleur moyenne des pixels de l'image d'origine.

2. Deuxième étape : *Fait partiellement* <br />
Effectuer un pré-traitement d'une base d'images.
Obtenir la couleur moyenne de toutes les images de la base et enregistrer les données dans un fichier CSV.

Pour le moment, la base est disponible. Elle contient 4320 images redimensionnées issues d'une base de données d'images : https://www.kaggle.com/alxmamaev/flowers-recognition <br />
Ces images sont disponibles dans un fichier compressé `ma_base_image.zip`. <br />
Pour travailler en ligne sur note_book, je n'ai mis en ligne que les 200 premières images.

2. Deuxième étape : (version alternative) (TODO) <br />
Effectuer un pré-traitement d'une base d'images.
Obtenir la couleur moyenne de toutes les images de la base et enregistrer les données **dans une base SQL**.

3. Troisième étape : (TODO) <br />
Remplacer chaque carré moyen de l'image par une image de la base qui a la couleur moyenne la plus proche.
Evidemment, plus la base est conséquente plus la photomosaïque est de qualité.
