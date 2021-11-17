# -*- coding: utf-8 -*-
"""
Created 18/09/20
@author: Guillaume Connan
"""

import os

def printFichiers(chemin: str) -> None:
    if not os.path.isdir(chemin):
        #ce n'est pas un répertoire donc c'est un fichier
        print(chemin)
    else:
        for sous_chemin in os.listdir(chemin):
            printFichiers(chemin + "/" + sous_chemin)
            
"""
Created 28/10/20
@author: David Cobac
"""

"""
import os
import sys


def parcours_repertoire(nom):
    contenu = os.listdir(nom)
    liste_fic = []
    liste_rep = []
    for c in contenu:
        if os.path.isdir(os.path.join(nom, c)):
            liste_rep.append(c)
        else:
            liste_fic.append(c)

    print(f"Dans {nom} :", liste_fic)
    for d in liste_rep:
        parcours_repertoire(os.path.join(nom, d))


rep = sys.argv[1]
parcours_repertoire(rep)
"""